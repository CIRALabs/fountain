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


class DeviceBody(object):
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
        'fqdn': 'str',
        'eui64': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'device_type_id': 'int',
        'manufacturer_id': 'int',
        'idev_id': 'str',
        'traffic_counts': 'DeviceBodyTrafficCounts',
        'mud_url': 'str',
        'profile_id': 'int',
        'current_vlan': 'str',
        'wan_enabled': 'bool',
        'lan_enabled': 'bool',
        'firewall_rules': 'list[object]',
        'firewall_rule_names': 'list[object]',
        'deleted': 'bool',
        'quaranteed': 'bool',
        'device_enabled': 'bool',
        'device_state': 'str',
        'failure_details': 'object',
        'ipv4': 'str',
        'ipv6': 'str',
        'acp_prefix': 'str',
        'idevid_hash': 'str',
        'ldevid': 'str',
        'ldevid_hash': 'str'
    }

    attribute_map = {
        'name': 'name',
        'fqdn': 'fqdn',
        'eui64': 'eui64',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'device_type_id': 'device_type_id',
        'manufacturer_id': 'manufacturer_id',
        'idev_id': 'idev_id',
        'traffic_counts': 'traffic_counts',
        'mud_url': 'mud_url',
        'profile_id': 'profile_id',
        'current_vlan': 'current_vlan',
        'wan_enabled': 'wan_enabled',
        'lan_enabled': 'lan_enabled',
        'firewall_rules': 'firewall_rules',
        'firewall_rule_names': 'firewall_rule_names',
        'deleted': 'deleted',
        'quaranteed': 'quaranteed',
        'device_enabled': 'device_enabled',
        'device_state': 'device_state',
        'failure_details': 'failure_details',
        'ipv4': 'ipv4',
        'ipv6': 'ipv6',
        'acp_prefix': 'acp_prefix',
        'idevid_hash': 'idevid_hash',
        'ldevid': 'ldevid',
        'ldevid_hash': 'ldevid_hash'
    }

    def __init__(self, name=None, fqdn=None, eui64=None, created_at=None, updated_at=None, device_type_id=None, manufacturer_id=None, idev_id=None, traffic_counts=None, mud_url=None, profile_id=None, current_vlan=None, wan_enabled=None, lan_enabled=None, firewall_rules=None, firewall_rule_names=None, deleted=False, quaranteed=None, device_enabled=None, device_state=None, failure_details=None, ipv4=None, ipv6=None, acp_prefix=None, idevid_hash=None, ldevid=None, ldevid_hash=None):  # noqa: E501
        """DeviceBody - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._fqdn = None
        self._eui64 = None
        self._created_at = None
        self._updated_at = None
        self._device_type_id = None
        self._manufacturer_id = None
        self._idev_id = None
        self._traffic_counts = None
        self._mud_url = None
        self._profile_id = None
        self._current_vlan = None
        self._wan_enabled = None
        self._lan_enabled = None
        self._firewall_rules = None
        self._firewall_rule_names = None
        self._deleted = None
        self._quaranteed = None
        self._device_enabled = None
        self._device_state = None
        self._failure_details = None
        self._ipv4 = None
        self._ipv6 = None
        self._acp_prefix = None
        self._idevid_hash = None
        self._ldevid = None
        self._ldevid_hash = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if fqdn is not None:
            self.fqdn = fqdn
        if eui64 is not None:
            self.eui64 = eui64
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if device_type_id is not None:
            self.device_type_id = device_type_id
        if manufacturer_id is not None:
            self.manufacturer_id = manufacturer_id
        if idev_id is not None:
            self.idev_id = idev_id
        if traffic_counts is not None:
            self.traffic_counts = traffic_counts
        if mud_url is not None:
            self.mud_url = mud_url
        if profile_id is not None:
            self.profile_id = profile_id
        if current_vlan is not None:
            self.current_vlan = current_vlan
        if wan_enabled is not None:
            self.wan_enabled = wan_enabled
        if lan_enabled is not None:
            self.lan_enabled = lan_enabled
        if firewall_rules is not None:
            self.firewall_rules = firewall_rules
        if firewall_rule_names is not None:
            self.firewall_rule_names = firewall_rule_names
        if deleted is not None:
            self.deleted = deleted
        if quaranteed is not None:
            self.quaranteed = quaranteed
        if device_enabled is not None:
            self.device_enabled = device_enabled
        if device_state is not None:
            self.device_state = device_state
        if failure_details is not None:
            self.failure_details = failure_details
        if ipv4 is not None:
            self.ipv4 = ipv4
        if ipv6 is not None:
            self.ipv6 = ipv6
        if acp_prefix is not None:
            self.acp_prefix = acp_prefix
        if idevid_hash is not None:
            self.idevid_hash = idevid_hash
        if ldevid is not None:
            self.ldevid = ldevid
        if ldevid_hash is not None:
            self.ldevid_hash = ldevid_hash

    @property
    def name(self):
        """Gets the name of this DeviceBody.  # noqa: E501

        Name of the device if available  # noqa: E501

        :return: The name of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceBody.

        Name of the device if available  # noqa: E501

        :param name: The name of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def fqdn(self):
        """Gets the fqdn of this DeviceBody.  # noqa: E501


        :return: The fqdn of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this DeviceBody.


        :param fqdn: The fqdn of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._fqdn = fqdn

    @property
    def eui64(self):
        """Gets the eui64 of this DeviceBody.  # noqa: E501


        :return: The eui64 of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._eui64

    @eui64.setter
    def eui64(self, eui64):
        """Sets the eui64 of this DeviceBody.


        :param eui64: The eui64 of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._eui64 = eui64

    @property
    def created_at(self):
        """Gets the created_at of this DeviceBody.  # noqa: E501

        Device creation datetime  # noqa: E501

        :return: The created_at of this DeviceBody.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DeviceBody.

        Device creation datetime  # noqa: E501

        :param created_at: The created_at of this DeviceBody.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DeviceBody.  # noqa: E501

        Device last update datetime  # noqa: E501

        :return: The updated_at of this DeviceBody.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DeviceBody.

        Device last update datetime  # noqa: E501

        :param updated_at: The updated_at of this DeviceBody.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def device_type_id(self):
        """Gets the device_type_id of this DeviceBody.  # noqa: E501


        :return: The device_type_id of this DeviceBody.  # noqa: E501
        :rtype: int
        """
        return self._device_type_id

    @device_type_id.setter
    def device_type_id(self, device_type_id):
        """Sets the device_type_id of this DeviceBody.


        :param device_type_id: The device_type_id of this DeviceBody.  # noqa: E501
        :type: int
        """

        self._device_type_id = device_type_id

    @property
    def manufacturer_id(self):
        """Gets the manufacturer_id of this DeviceBody.  # noqa: E501


        :return: The manufacturer_id of this DeviceBody.  # noqa: E501
        :rtype: int
        """
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        """Sets the manufacturer_id of this DeviceBody.


        :param manufacturer_id: The manufacturer_id of this DeviceBody.  # noqa: E501
        :type: int
        """

        self._manufacturer_id = manufacturer_id

    @property
    def idev_id(self):
        """Gets the idev_id of this DeviceBody.  # noqa: E501


        :return: The idev_id of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._idev_id

    @idev_id.setter
    def idev_id(self, idev_id):
        """Sets the idev_id of this DeviceBody.


        :param idev_id: The idev_id of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._idev_id = idev_id

    @property
    def traffic_counts(self):
        """Gets the traffic_counts of this DeviceBody.  # noqa: E501


        :return: The traffic_counts of this DeviceBody.  # noqa: E501
        :rtype: DeviceBodyTrafficCounts
        """
        return self._traffic_counts

    @traffic_counts.setter
    def traffic_counts(self, traffic_counts):
        """Sets the traffic_counts of this DeviceBody.


        :param traffic_counts: The traffic_counts of this DeviceBody.  # noqa: E501
        :type: DeviceBodyTrafficCounts
        """

        self._traffic_counts = traffic_counts

    @property
    def mud_url(self):
        """Gets the mud_url of this DeviceBody.  # noqa: E501


        :return: The mud_url of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._mud_url

    @mud_url.setter
    def mud_url(self, mud_url):
        """Sets the mud_url of this DeviceBody.


        :param mud_url: The mud_url of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._mud_url = mud_url

    @property
    def profile_id(self):
        """Gets the profile_id of this DeviceBody.  # noqa: E501


        :return: The profile_id of this DeviceBody.  # noqa: E501
        :rtype: int
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this DeviceBody.


        :param profile_id: The profile_id of this DeviceBody.  # noqa: E501
        :type: int
        """

        self._profile_id = profile_id

    @property
    def current_vlan(self):
        """Gets the current_vlan of this DeviceBody.  # noqa: E501


        :return: The current_vlan of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._current_vlan

    @current_vlan.setter
    def current_vlan(self, current_vlan):
        """Sets the current_vlan of this DeviceBody.


        :param current_vlan: The current_vlan of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._current_vlan = current_vlan

    @property
    def wan_enabled(self):
        """Gets the wan_enabled of this DeviceBody.  # noqa: E501


        :return: The wan_enabled of this DeviceBody.  # noqa: E501
        :rtype: bool
        """
        return self._wan_enabled

    @wan_enabled.setter
    def wan_enabled(self, wan_enabled):
        """Sets the wan_enabled of this DeviceBody.


        :param wan_enabled: The wan_enabled of this DeviceBody.  # noqa: E501
        :type: bool
        """

        self._wan_enabled = wan_enabled

    @property
    def lan_enabled(self):
        """Gets the lan_enabled of this DeviceBody.  # noqa: E501


        :return: The lan_enabled of this DeviceBody.  # noqa: E501
        :rtype: bool
        """
        return self._lan_enabled

    @lan_enabled.setter
    def lan_enabled(self, lan_enabled):
        """Sets the lan_enabled of this DeviceBody.


        :param lan_enabled: The lan_enabled of this DeviceBody.  # noqa: E501
        :type: bool
        """

        self._lan_enabled = lan_enabled

    @property
    def firewall_rules(self):
        """Gets the firewall_rules of this DeviceBody.  # noqa: E501


        :return: The firewall_rules of this DeviceBody.  # noqa: E501
        :rtype: list[object]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this DeviceBody.


        :param firewall_rules: The firewall_rules of this DeviceBody.  # noqa: E501
        :type: list[object]
        """

        self._firewall_rules = firewall_rules

    @property
    def firewall_rule_names(self):
        """Gets the firewall_rule_names of this DeviceBody.  # noqa: E501


        :return: The firewall_rule_names of this DeviceBody.  # noqa: E501
        :rtype: list[object]
        """
        return self._firewall_rule_names

    @firewall_rule_names.setter
    def firewall_rule_names(self, firewall_rule_names):
        """Sets the firewall_rule_names of this DeviceBody.


        :param firewall_rule_names: The firewall_rule_names of this DeviceBody.  # noqa: E501
        :type: list[object]
        """

        self._firewall_rule_names = firewall_rule_names

    @property
    def deleted(self):
        """Gets the deleted of this DeviceBody.  # noqa: E501


        :return: The deleted of this DeviceBody.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this DeviceBody.


        :param deleted: The deleted of this DeviceBody.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def quaranteed(self):
        """Gets the quaranteed of this DeviceBody.  # noqa: E501


        :return: The quaranteed of this DeviceBody.  # noqa: E501
        :rtype: bool
        """
        return self._quaranteed

    @quaranteed.setter
    def quaranteed(self, quaranteed):
        """Sets the quaranteed of this DeviceBody.


        :param quaranteed: The quaranteed of this DeviceBody.  # noqa: E501
        :type: bool
        """

        self._quaranteed = quaranteed

    @property
    def device_enabled(self):
        """Gets the device_enabled of this DeviceBody.  # noqa: E501


        :return: The device_enabled of this DeviceBody.  # noqa: E501
        :rtype: bool
        """
        return self._device_enabled

    @device_enabled.setter
    def device_enabled(self, device_enabled):
        """Sets the device_enabled of this DeviceBody.


        :param device_enabled: The device_enabled of this DeviceBody.  # noqa: E501
        :type: bool
        """

        self._device_enabled = device_enabled

    @property
    def device_state(self):
        """Gets the device_state of this DeviceBody.  # noqa: E501


        :return: The device_state of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._device_state

    @device_state.setter
    def device_state(self, device_state):
        """Sets the device_state of this DeviceBody.


        :param device_state: The device_state of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._device_state = device_state

    @property
    def failure_details(self):
        """Gets the failure_details of this DeviceBody.  # noqa: E501


        :return: The failure_details of this DeviceBody.  # noqa: E501
        :rtype: object
        """
        return self._failure_details

    @failure_details.setter
    def failure_details(self, failure_details):
        """Sets the failure_details of this DeviceBody.


        :param failure_details: The failure_details of this DeviceBody.  # noqa: E501
        :type: object
        """

        self._failure_details = failure_details

    @property
    def ipv4(self):
        """Gets the ipv4 of this DeviceBody.  # noqa: E501


        :return: The ipv4 of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """Sets the ipv4 of this DeviceBody.


        :param ipv4: The ipv4 of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._ipv4 = ipv4

    @property
    def ipv6(self):
        """Gets the ipv6 of this DeviceBody.  # noqa: E501


        :return: The ipv6 of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this DeviceBody.


        :param ipv6: The ipv6 of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._ipv6 = ipv6

    @property
    def acp_prefix(self):
        """Gets the acp_prefix of this DeviceBody.  # noqa: E501


        :return: The acp_prefix of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._acp_prefix

    @acp_prefix.setter
    def acp_prefix(self, acp_prefix):
        """Sets the acp_prefix of this DeviceBody.


        :param acp_prefix: The acp_prefix of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._acp_prefix = acp_prefix

    @property
    def idevid_hash(self):
        """Gets the idevid_hash of this DeviceBody.  # noqa: E501


        :return: The idevid_hash of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._idevid_hash

    @idevid_hash.setter
    def idevid_hash(self, idevid_hash):
        """Sets the idevid_hash of this DeviceBody.


        :param idevid_hash: The idevid_hash of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._idevid_hash = idevid_hash

    @property
    def ldevid(self):
        """Gets the ldevid of this DeviceBody.  # noqa: E501


        :return: The ldevid of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._ldevid

    @ldevid.setter
    def ldevid(self, ldevid):
        """Sets the ldevid of this DeviceBody.


        :param ldevid: The ldevid of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._ldevid = ldevid

    @property
    def ldevid_hash(self):
        """Gets the ldevid_hash of this DeviceBody.  # noqa: E501


        :return: The ldevid_hash of this DeviceBody.  # noqa: E501
        :rtype: str
        """
        return self._ldevid_hash

    @ldevid_hash.setter
    def ldevid_hash(self, ldevid_hash):
        """Sets the ldevid_hash of this DeviceBody.


        :param ldevid_hash: The ldevid_hash of this DeviceBody.  # noqa: E501
        :type: str
        """

        self._ldevid_hash = ldevid_hash

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
        if not isinstance(other, DeviceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
