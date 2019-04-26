# coding: utf-8

"""
    CIRA SHG Windex API

    CIRALabs SecureHomeGateway Windex API: between smartphone and router  # noqa: E501

    OpenAPI spec version: 1.0.0-current
    Contact: securehomegateway@cira.ca
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ManufacturerBody(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'masa_url': 'str',
        'issuer_public_key': 'str',
        'trust': 'str',
        'issuer_dn': 'str'
    }

    attribute_map = {
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'masa_url': 'masa_url',
        'issuer_public_key': 'issuer_public_key',
        'trust': 'trust',
        'issuer_dn': 'issuer_dn'
    }

    def __init__(self, name=None, created_at=None, updated_at=None, masa_url=None, issuer_public_key=None, trust='unknown', issuer_dn=None):  # noqa: E501
        """ManufacturerBody - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._created_at = None
        self._updated_at = None
        self._masa_url = None
        self._issuer_public_key = None
        self._trust = None
        self._issuer_dn = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if masa_url is not None:
            self.masa_url = masa_url
        if issuer_public_key is not None:
            self.issuer_public_key = issuer_public_key
        if trust is not None:
            self.trust = trust
        if issuer_dn is not None:
            self.issuer_dn = issuer_dn

    @property
    def name(self):
        """Gets the name of this ManufacturerBody.  # noqa: E501

        Name of the manufacturer  # noqa: E501

        :return: The name of this ManufacturerBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ManufacturerBody.

        Name of the manufacturer  # noqa: E501

        :param name: The name of this ManufacturerBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this ManufacturerBody.  # noqa: E501

        Manufacturer creation datetime  # noqa: E501

        :return: The created_at of this ManufacturerBody.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ManufacturerBody.

        Manufacturer creation datetime  # noqa: E501

        :param created_at: The created_at of this ManufacturerBody.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ManufacturerBody.  # noqa: E501

        Manufacturer last update datetime  # noqa: E501

        :return: The updated_at of this ManufacturerBody.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ManufacturerBody.

        Manufacturer last update datetime  # noqa: E501

        :param updated_at: The updated_at of this ManufacturerBody.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def masa_url(self):
        """Gets the masa_url of this ManufacturerBody.  # noqa: E501


        :return: The masa_url of this ManufacturerBody.  # noqa: E501
        :rtype: str
        """
        return self._masa_url

    @masa_url.setter
    def masa_url(self, masa_url):
        """Sets the masa_url of this ManufacturerBody.


        :param masa_url: The masa_url of this ManufacturerBody.  # noqa: E501
        :type: str
        """

        self._masa_url = masa_url

    @property
    def issuer_public_key(self):
        """Gets the issuer_public_key of this ManufacturerBody.  # noqa: E501


        :return: The issuer_public_key of this ManufacturerBody.  # noqa: E501
        :rtype: str
        """
        return self._issuer_public_key

    @issuer_public_key.setter
    def issuer_public_key(self, issuer_public_key):
        """Sets the issuer_public_key of this ManufacturerBody.


        :param issuer_public_key: The issuer_public_key of this ManufacturerBody.  # noqa: E501
        :type: str
        """

        self._issuer_public_key = issuer_public_key

    @property
    def trust(self):
        """Gets the trust of this ManufacturerBody.  # noqa: E501

        unknown: The manufacturer's status is unknown. firstused: The manufacturer's has been seen by issuer_dn, but is otherwise unknown. admin: A manufacturer that has been marked by the admin as trusted for pure-EST (no BRSKI) enrollment. brski: A manufacturer that will do BRSKI voucher-request/voucher process. webpki: Probably not useful, not well defined.   # noqa: E501

        :return: The trust of this ManufacturerBody.  # noqa: E501
        :rtype: str
        """
        return self._trust

    @trust.setter
    def trust(self, trust):
        """Sets the trust of this ManufacturerBody.

        unknown: The manufacturer's status is unknown. firstused: The manufacturer's has been seen by issuer_dn, but is otherwise unknown. admin: A manufacturer that has been marked by the admin as trusted for pure-EST (no BRSKI) enrollment. brski: A manufacturer that will do BRSKI voucher-request/voucher process. webpki: Probably not useful, not well defined.   # noqa: E501

        :param trust: The trust of this ManufacturerBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["unknown", "firstused", "admin", "brski", "webpki"]  # noqa: E501
        if trust not in allowed_values:
            raise ValueError(
                "Invalid value for `trust` ({0}), must be one of {1}"  # noqa: E501
                .format(trust, allowed_values)
            )

        self._trust = trust

    @property
    def issuer_dn(self):
        """Gets the issuer_dn of this ManufacturerBody.  # noqa: E501


        :return: The issuer_dn of this ManufacturerBody.  # noqa: E501
        :rtype: str
        """
        return self._issuer_dn

    @issuer_dn.setter
    def issuer_dn(self, issuer_dn):
        """Sets the issuer_dn of this ManufacturerBody.


        :param issuer_dn: The issuer_dn of this ManufacturerBody.  # noqa: E501
        :type: str
        """

        self._issuer_dn = issuer_dn

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ManufacturerBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
