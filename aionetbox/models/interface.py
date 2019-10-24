# coding: utf-8

"""
    NetBox API

    API to access NetBox  # noqa: E501

    OpenAPI spec version: 2.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from aionetbox.models.connection_status import ConnectionStatus  # noqa: F401,E501
from aionetbox.models.nested_cable import NestedCable  # noqa: F401,E501
from aionetbox.models.nested_device import NestedDevice  # noqa: F401,E501
from aionetbox.models.nested_interface import NestedInterface  # noqa: F401,E501
from aionetbox.models.nested_vlan import NestedVLAN  # noqa: F401,E501
from aionetbox.models.status import Status  # noqa: F401,E501


class Interface(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'device': 'NestedDevice',
        'name': 'str',
        'type': 'Status',
        'form_factor': 'Status',
        'enabled': 'bool',
        'lag': 'NestedInterface',
        'mtu': 'int',
        'mac_address': 'str',
        'mgmt_only': 'bool',
        'description': 'str',
        'connected_endpoint_type': 'str',
        'connected_endpoint': 'dict(str, str)',
        'connection_status': 'ConnectionStatus',
        'cable': 'NestedCable',
        'mode': 'Status',
        'untagged_vlan': 'NestedVLAN',
        'tagged_vlans': 'list[NestedVLAN]',
        'tags': 'list[str]',
        'count_ipaddresses': 'str'
    }

    attribute_map = {
        'id': 'id',
        'device': 'device',
        'name': 'name',
        'type': 'type',
        'form_factor': 'form_factor',
        'enabled': 'enabled',
        'lag': 'lag',
        'mtu': 'mtu',
        'mac_address': 'mac_address',
        'mgmt_only': 'mgmt_only',
        'description': 'description',
        'connected_endpoint_type': 'connected_endpoint_type',
        'connected_endpoint': 'connected_endpoint',
        'connection_status': 'connection_status',
        'cable': 'cable',
        'mode': 'mode',
        'untagged_vlan': 'untagged_vlan',
        'tagged_vlans': 'tagged_vlans',
        'tags': 'tags',
        'count_ipaddresses': 'count_ipaddresses'
    }

    def __init__(self, id=None, device=None, name=None, type=None, form_factor=None, enabled=None, lag=None, mtu=None, mac_address=None, mgmt_only=None, description=None, connected_endpoint_type=None, connected_endpoint=None, connection_status=None, cable=None, mode=None, untagged_vlan=None, tagged_vlans=None, tags=None, count_ipaddresses=None):  # noqa: E501
        """Interface - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._device = None
        self._name = None
        self._type = None
        self._form_factor = None
        self._enabled = None
        self._lag = None
        self._mtu = None
        self._mac_address = None
        self._mgmt_only = None
        self._description = None
        self._connected_endpoint_type = None
        self._connected_endpoint = None
        self._connection_status = None
        self._cable = None
        self._mode = None
        self._untagged_vlan = None
        self._tagged_vlans = None
        self._tags = None
        self._count_ipaddresses = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.device = device
        self.name = name
        if type is not None:
            self.type = type
        if form_factor is not None:
            self.form_factor = form_factor
        if enabled is not None:
            self.enabled = enabled
        if lag is not None:
            self.lag = lag
        if mtu is not None:
            self.mtu = mtu
        if mac_address is not None:
            self.mac_address = mac_address
        if mgmt_only is not None:
            self.mgmt_only = mgmt_only
        if description is not None:
            self.description = description
        if connected_endpoint_type is not None:
            self.connected_endpoint_type = connected_endpoint_type
        if connected_endpoint is not None:
            self.connected_endpoint = connected_endpoint
        if connection_status is not None:
            self.connection_status = connection_status
        if cable is not None:
            self.cable = cable
        if mode is not None:
            self.mode = mode
        if untagged_vlan is not None:
            self.untagged_vlan = untagged_vlan
        if tagged_vlans is not None:
            self.tagged_vlans = tagged_vlans
        if tags is not None:
            self.tags = tags
        if count_ipaddresses is not None:
            self.count_ipaddresses = count_ipaddresses

    @property
    def id(self):
        """Gets the id of this Interface.  # noqa: E501


        :return: The id of this Interface.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Interface.


        :param id: The id of this Interface.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device(self):
        """Gets the device of this Interface.  # noqa: E501


        :return: The device of this Interface.  # noqa: E501
        :rtype: NestedDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this Interface.


        :param device: The device of this Interface.  # noqa: E501
        :type: NestedDevice
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def name(self):
        """Gets the name of this Interface.  # noqa: E501


        :return: The name of this Interface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Interface.


        :param name: The name of this Interface.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this Interface.  # noqa: E501


        :return: The type of this Interface.  # noqa: E501
        :rtype: Status
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Interface.


        :param type: The type of this Interface.  # noqa: E501
        :type: Status
        """

        self._type = type

    @property
    def form_factor(self):
        """Gets the form_factor of this Interface.  # noqa: E501


        :return: The form_factor of this Interface.  # noqa: E501
        :rtype: Status
        """
        return self._form_factor

    @form_factor.setter
    def form_factor(self, form_factor):
        """Sets the form_factor of this Interface.


        :param form_factor: The form_factor of this Interface.  # noqa: E501
        :type: Status
        """

        self._form_factor = form_factor

    @property
    def enabled(self):
        """Gets the enabled of this Interface.  # noqa: E501


        :return: The enabled of this Interface.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Interface.


        :param enabled: The enabled of this Interface.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def lag(self):
        """Gets the lag of this Interface.  # noqa: E501


        :return: The lag of this Interface.  # noqa: E501
        :rtype: NestedInterface
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        """Sets the lag of this Interface.


        :param lag: The lag of this Interface.  # noqa: E501
        :type: NestedInterface
        """

        self._lag = lag

    @property
    def mtu(self):
        """Gets the mtu of this Interface.  # noqa: E501


        :return: The mtu of this Interface.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this Interface.


        :param mtu: The mtu of this Interface.  # noqa: E501
        :type: int
        """
        if mtu is not None and mtu > 65536:  # noqa: E501
            raise ValueError("Invalid value for `mtu`, must be a value less than or equal to `65536`")  # noqa: E501
        if mtu is not None and mtu < 1:  # noqa: E501
            raise ValueError("Invalid value for `mtu`, must be a value greater than or equal to `1`")  # noqa: E501

        self._mtu = mtu

    @property
    def mac_address(self):
        """Gets the mac_address of this Interface.  # noqa: E501


        :return: The mac_address of this Interface.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this Interface.


        :param mac_address: The mac_address of this Interface.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def mgmt_only(self):
        """Gets the mgmt_only of this Interface.  # noqa: E501

        This interface is used only for out-of-band management  # noqa: E501

        :return: The mgmt_only of this Interface.  # noqa: E501
        :rtype: bool
        """
        return self._mgmt_only

    @mgmt_only.setter
    def mgmt_only(self, mgmt_only):
        """Sets the mgmt_only of this Interface.

        This interface is used only for out-of-band management  # noqa: E501

        :param mgmt_only: The mgmt_only of this Interface.  # noqa: E501
        :type: bool
        """

        self._mgmt_only = mgmt_only

    @property
    def description(self):
        """Gets the description of this Interface.  # noqa: E501


        :return: The description of this Interface.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Interface.


        :param description: The description of this Interface.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def connected_endpoint_type(self):
        """Gets the connected_endpoint_type of this Interface.  # noqa: E501


        :return: The connected_endpoint_type of this Interface.  # noqa: E501
        :rtype: str
        """
        return self._connected_endpoint_type

    @connected_endpoint_type.setter
    def connected_endpoint_type(self, connected_endpoint_type):
        """Sets the connected_endpoint_type of this Interface.


        :param connected_endpoint_type: The connected_endpoint_type of this Interface.  # noqa: E501
        :type: str
        """

        self._connected_endpoint_type = connected_endpoint_type

    @property
    def connected_endpoint(self):
        """Gets the connected_endpoint of this Interface.  # noqa: E501

                 Return the appropriate serializer for the type of connected object.           # noqa: E501

        :return: The connected_endpoint of this Interface.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._connected_endpoint

    @connected_endpoint.setter
    def connected_endpoint(self, connected_endpoint):
        """Sets the connected_endpoint of this Interface.

                 Return the appropriate serializer for the type of connected object.           # noqa: E501

        :param connected_endpoint: The connected_endpoint of this Interface.  # noqa: E501
        :type: dict(str, str)
        """

        self._connected_endpoint = connected_endpoint

    @property
    def connection_status(self):
        """Gets the connection_status of this Interface.  # noqa: E501


        :return: The connection_status of this Interface.  # noqa: E501
        :rtype: ConnectionStatus
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this Interface.


        :param connection_status: The connection_status of this Interface.  # noqa: E501
        :type: ConnectionStatus
        """

        self._connection_status = connection_status

    @property
    def cable(self):
        """Gets the cable of this Interface.  # noqa: E501


        :return: The cable of this Interface.  # noqa: E501
        :rtype: NestedCable
        """
        return self._cable

    @cable.setter
    def cable(self, cable):
        """Sets the cable of this Interface.


        :param cable: The cable of this Interface.  # noqa: E501
        :type: NestedCable
        """

        self._cable = cable

    @property
    def mode(self):
        """Gets the mode of this Interface.  # noqa: E501


        :return: The mode of this Interface.  # noqa: E501
        :rtype: Status
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Interface.


        :param mode: The mode of this Interface.  # noqa: E501
        :type: Status
        """

        self._mode = mode

    @property
    def untagged_vlan(self):
        """Gets the untagged_vlan of this Interface.  # noqa: E501


        :return: The untagged_vlan of this Interface.  # noqa: E501
        :rtype: NestedVLAN
        """
        return self._untagged_vlan

    @untagged_vlan.setter
    def untagged_vlan(self, untagged_vlan):
        """Sets the untagged_vlan of this Interface.


        :param untagged_vlan: The untagged_vlan of this Interface.  # noqa: E501
        :type: NestedVLAN
        """

        self._untagged_vlan = untagged_vlan

    @property
    def tagged_vlans(self):
        """Gets the tagged_vlans of this Interface.  # noqa: E501


        :return: The tagged_vlans of this Interface.  # noqa: E501
        :rtype: list[NestedVLAN]
        """
        return self._tagged_vlans

    @tagged_vlans.setter
    def tagged_vlans(self, tagged_vlans):
        """Sets the tagged_vlans of this Interface.


        :param tagged_vlans: The tagged_vlans of this Interface.  # noqa: E501
        :type: list[NestedVLAN]
        """

        self._tagged_vlans = tagged_vlans

    @property
    def tags(self):
        """Gets the tags of this Interface.  # noqa: E501


        :return: The tags of this Interface.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Interface.


        :param tags: The tags of this Interface.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def count_ipaddresses(self):
        """Gets the count_ipaddresses of this Interface.  # noqa: E501


        :return: The count_ipaddresses of this Interface.  # noqa: E501
        :rtype: str
        """
        return self._count_ipaddresses

    @count_ipaddresses.setter
    def count_ipaddresses(self, count_ipaddresses):
        """Sets the count_ipaddresses of this Interface.


        :param count_ipaddresses: The count_ipaddresses of this Interface.  # noqa: E501
        :type: str
        """

        self._count_ipaddresses = count_ipaddresses

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Interface, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Interface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
