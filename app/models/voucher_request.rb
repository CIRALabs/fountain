class VoucherRequest < ApplicationRecord

  belongs_to :node
  belongs_to :manufacturer
  has_many   :vouchers

  attr_accessor :certificate, :issuer_pki, :request

  class InvalidVoucherRequest < Exception; end
  class MissingPublicKey < Exception; end
  class BadMASA          < Exception; end

  def self.from_json(json, signed = false)
    vr = CmsVoucherRequest.create(details: json, signed: signed)
    vr.populate_explicit_fields
    vr
  end

  def self.from_cbor(hash, signed = false)
    vr = CoseVoucherRequest.create(vdetails: hash, signed: signed)
    vr.populate_explicit_fields
    vr
  end

  def self.from_json_jose(token, json)
    signed = false
    vr = Chariwt::VoucherRequest.from_json_jose(token)
    if vr
      signed = true
      json = vr.vrhash
    end
    voucher = from_json(json, signed)
    voucher.request = vr
    return voucher
  end

  def self.from_cose_cbor(token, pubkey = nil)
    signed = false
    vr = Chariwt::VoucherRequest.from_cose_cbor(token, pubkey)
    if vr
      signed = true
      hash = vr.vrhash
    end
    voucher = from_cbor(hash, signed)
    voucher.request = vr
    voucher.pledge_request = token
    return voucher
  end

  def self.from_pkcs7(token, json = nil)
    signed = false
    vr = Chariwt::VoucherRequest.from_pkcs7(token)
    if vr
      signed = true
      json = vr.vrhash
    end
    voucher = from_json(json, signed)
    voucher.request = vr
    voucher.pledge_request = token
    return voucher
  end

  def self.from_pkcs7_withoutkey(token, json = nil)
    signed = false
    begin
      vr = Chariwt::VoucherRequest.from_pkcs7_withoutkey(token)
    rescue Chariwt::Voucher::RequestFailedValidation
      raise VoucherRequest::InvalidVoucherRequest
    end
    if vr
      signed = true
      json = vr.vrhash
    end
    voucher = from_json(json, signed)
    voucher.request = vr
    voucher.pledge_request = token
    return voucher
  end

  def vdetails=(x)
    @vdetails = x
  end

  def vdetails
    unless @vdetails
      return nil unless details
      raise VoucherRequest::InvalidVoucherRequest unless details["ietf-voucher-request:voucher"]
      @vdetails = details["ietf-voucher-request:voucher"]
    end
    @vdetails
  end

  def name
    "voucherreq_#{self.id}"
  end
  def savefixturefw(fw)
    voucher.savefixturefw(fw) if voucher
    owner.savefixturefw(fw)   if owner
    save_self_tofixture(fw)
  end

  def populate_explicit_fields
    self.device_identifier = vdetails["serial-number"]
    self.node              = Node.find_or_make_by_number(device_identifier)
    self.nonce             = vdetails["nonce"]
  end

  # create a voucher request (JOSE signed JSON) appropriate for sending to the MASA.
  # it shall always be signed.
  def registrar_voucher_request_json
    # now build our voucher request from the one we got.
    vreq = Chariwt::VoucherRequest.new
    vreq.signing_cert = FountainKeys.ca.jrc_pub_key
    vreq.nonce      = nonce
    vreq.serialNumber = device_identifier
    vreq.createdOn  = created_at
    vreq.assertion  = :proximity
    vreq.priorSignedVoucherRequest = pledge_request
    self.request = vreq
    jwt = vreq.jose_sign(FountainKeys.ca.jrc_priv_key)
  end

  def signing_cert
    request.try(:signing_cert)
  end

  def registrar_voucher_request
    raise InvalidVoucherRequest
  end

  def registrar_voucher_request_type
    raise InvalidVoucherRequest
  end

  def certificate
    if !@certificate and !tls_clientcert.blank?
      @certificate   ||= OpenSSL::X509::Certificate.new(tls_clientcert)
    end
    @certificate   ||= signing_cert
    @certificate
  end

  def issuer_pki
    @issuer_pki  ||= certificate.issuer.to_der
  end

  def discover_manufacturer
    @masa_url = nil
    manu = nil
    return nil unless certificate
    certificate.extensions.each { |ext|
      if ext.oid == "1.3.6.1.4.1.46930.2"
        @masa_url = ext.value[2..-1]
      end
    }
    if @masa_url
      manu = Manufacturer.where(masa_url: @masa_url).take
      unless manu
        # try again with trailing /
        manu = Manufacturer.where(masa_url: @masa_url + "/").take
      end
    else
      logger.warn "Did not find a MASA URL extension"
      unless manu
        logger.warn "Tried to find manufacturer by issuer #{certificate.issuer.to_s}"
        manu = Manufacturer.where(issuer_public_key: issuer_pki).take
      end
    end
    unless manu
      manu = Manufacturer.create(masa_url: @masa_url,
                                 issuer_public_key: issuer_pki)
      manu.name = "Manu#{manu.id}"
      manu.save!
    end

    self.manufacturer = manu
  end

  def masa_url
    manufacturer.try(:masa_url)
  end
  def masa_uri(url = nil)
    url ||= masa_url
    @masauri ||= URI::join(url, "/.well-known/est/requestvoucher")
  end
  def http_handler
    @http_handler ||=
      Net::HTTP.start(masa_uri.host, masa_uri.port,
                      { :verify_mode => OpenSSL::SSL::VERIFY_NONE,
                        :use_ssl => masa_uri.scheme == 'https'})
  end

  def process_content_type_arguments(args)
    args.each { |param|
      param.strip!
      (thing,value) = param.split(/=/)
      case thing.downcase
      when 'smime-type'
        @smimetype = value.downcase
        process_smime_type
        @responsetype = :pkcs7_voucher
      end
    }
  end

  def process_smime_type
    case @smimetype.downcase
    when 'voucher'
      @pkcs7voucher = true
      @voucher_response_type = :pkcs7
    end
  end

  def process_content_type(value)
    things = value.split(/;/)
    majortype = things.shift
    return false unless majortype

    @apptype = majortype.downcase
    case @apptype
    when 'application/pkcs7-mime'
      @pkcs7 = true
      process_content_type_arguments(things)
      return true
    when 'application/cms'
      @pkcs7 = true
      process_content_type_arguments(things)
      return true
    when 'application/cbor+cms'
      @cose = true
      @pkcs7 = false
      return true
    end
  end
  def response_pkcs7?
    @pkcs7
  end
  def response_voucher?
    @pkcs7voucher
  end
  def response_type
    @responsetype
  end

  def decode_pem(base64stuff)
    begin
      der = Base64.urlsafe_decode64(base64stuff)
    rescue ArgumentError
      der = Base64.decode64(base64stuff)
    end
  end

  def get_voucher(target_url = nil)
    target_uri = masa_uri(target_url)

    puts "Contacting server at: #{target_uri} about #{self.device_identifier}"

    request = Net::HTTP::Post.new(target_uri)
    request.body         = registrar_voucher_request
    request.content_type = registrar_voucher_request_type
    response = http_handler.request request # Net::HTTPResponse object

    case response
    when Net::HTTPBadRequest
      raise VoucherRequest::BadMASA.new("bad request")

    when Net::HTTPNotFound
      raise VoucherRequest::BadMASA.new(response.body)

    when Net::HTTPNotFound
      logger.info "MASA at #{target_uri} says #{response.message}"
      raise VoucherRequest::BadMASA.new(response.message)

    when Net::HTTPSuccess
      if process_content_type(@content_type = response['Content-Type'])

        case
        when @pkcs7
          der = decode_pem(response.body)
          voucher = ::CmsVoucher.from_voucher(@voucher_response_type, der)

        when @cose
          voucher = ::CoseVoucher.from_voucher(@voucher_response_type, response.body)

        else
          raise Voucher::UnknownVoucherType
        end
        voucher.voucher_request = self
        voucher.node = self.node
        voucher.manufacturer = self.manufacturer
        voucher.save!
        return voucher
      else
        puts "Content type #{response['Content-Type']} is wrong"
        nil
      end

    when Net::HTTPRedirection
      nil
    end

    return nil
  end
end

