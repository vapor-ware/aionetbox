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


class WritableVirtualMachineInterface(object):
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
        'virtual_machine': 'int',
        'name': 'str',
        'type': 'int',
        'enabled': 'bool',
        'mtu': 'int',
        'mac_address': 'str',
        'description': 'str',
        'mode': 'int',
        'untagged_vlan': 'int',
        'tagged_vlans': 'list[int]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'virtual_machine': 'virtual_machine',
        'name': 'name',
        'type': 'type',
        'enabled': 'enabled',
        'mtu': 'mtu',
        'mac_address': 'mac_address',
        'description': 'description',
        'mode': 'mode',
        'untagged_vlan': 'untagged_vlan',
        'tagged_vlans': 'tagged_vlans',
        'tags': 'tags'
    }

    def __init__(self, id=None, virtual_machine=None, name=None, type=None, enabled=None, mtu=None, mac_address=None, description=None, mode=None, untagged_vlan=None, tagged_vlans=None, tags=None):  # noqa: E501
        """WritableVirtualMachineInterface - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._virtual_machine = None
        self._name = None
        self._type = None
        self._enabled = None
        self._mtu = None
        self._mac_address = None
        self._description = None
        self._mode = None
        self._untagged_vlan = None
        self._tagged_vlans = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if virtual_machine is not None:
            self.virtual_machine = virtual_machine
        self.name = name
        if type is not None:
            self.type = type
        if enabled is not None:
            self.enabled = enabled
        if mtu is not None:
            self.mtu = mtu
        if mac_address is not None:
            self.mac_address = mac_address
        if description is not None:
            self.description = description
        if mode is not None:
            self.mode = mode
        if untagged_vlan is not None:
            self.untagged_vlan = untagged_vlan
        if tagged_vlans is not None:
            self.tagged_vlans = tagged_vlans
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The id of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WritableVirtualMachineInterface.


        :param id: The id of this WritableVirtualMachineInterface.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def virtual_machine(self):
        """Gets the virtual_machine of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The virtual_machine of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: int
        """
        return self._virtual_machine

    @virtual_machine.setter
    def virtual_machine(self, virtual_machine):
        """Sets the virtual_machine of this WritableVirtualMachineInterface.


        :param virtual_machine: The virtual_machine of this WritableVirtualMachineInterface.  # noqa: E501
        :type: int
        """

        self._virtual_machine = virtual_machine

    @property
    def name(self):
        """Gets the name of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The name of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WritableVirtualMachineInterface.


        :param name: The name of this WritableVirtualMachineInterface.  # noqa: E501
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
        """Gets the type of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The type of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WritableVirtualMachineInterface.


        :param type: The type of this WritableVirtualMachineInterface.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def enabled(self):
        """Gets the enabled of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The enabled of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this WritableVirtualMachineInterface.


        :param enabled: The enabled of this WritableVirtualMachineInterface.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def mtu(self):
        """Gets the mtu of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The mtu of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this WritableVirtualMachineInterface.


        :param mtu: The mtu of this WritableVirtualMachineInterface.  # noqa: E501
        :type: int
        """
        if mtu is not None and mtu > 65536:  # noqa: E501
            raise ValueError("Invalid value for `mtu`, must be a value less than or equal to `65536`")  # noqa: E501
        if mtu is not None and mtu < 1:  # noqa: E501
            raise ValueError("Invalid value for `mtu`, must be a value greater than or equal to `1`")  # noqa: E501

        self._mtu = mtu

    @property
    def mac_address(self):
        """Gets the mac_address of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The mac_address of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this WritableVirtualMachineInterface.


        :param mac_address: The mac_address of this WritableVirtualMachineInterface.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def description(self):
        """Gets the description of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The description of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WritableVirtualMachineInterface.


        :param description: The description of this WritableVirtualMachineInterface.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def mode(self):
        """Gets the mode of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The mode of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this WritableVirtualMachineInterface.


        :param mode: The mode of this WritableVirtualMachineInterface.  # noqa: E501
        :type: int
        """

        self._mode = mode

    @property
    def untagged_vlan(self):
        """Gets the untagged_vlan of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The untagged_vlan of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: int
        """
        return self._untagged_vlan

    @untagged_vlan.setter
    def untagged_vlan(self, untagged_vlan):
        """Sets the untagged_vlan of this WritableVirtualMachineInterface.


        :param untagged_vlan: The untagged_vlan of this WritableVirtualMachineInterface.  # noqa: E501
        :type: int
        """

        self._untagged_vlan = untagged_vlan

    @property
    def tagged_vlans(self):
        """Gets the tagged_vlans of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The tagged_vlans of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: list[int]
        """
        return self._tagged_vlans

    @tagged_vlans.setter
    def tagged_vlans(self, tagged_vlans):
        """Sets the tagged_vlans of this WritableVirtualMachineInterface.


        :param tagged_vlans: The tagged_vlans of this WritableVirtualMachineInterface.  # noqa: E501
        :type: list[int]
        """

        self._tagged_vlans = tagged_vlans

    @property
    def tags(self):
        """Gets the tags of this WritableVirtualMachineInterface.  # noqa: E501


        :return: The tags of this WritableVirtualMachineInterface.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WritableVirtualMachineInterface.


        :param tags: The tags of this WritableVirtualMachineInterface.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if issubclass(WritableVirtualMachineInterface, dict):
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
        if not isinstance(other, WritableVirtualMachineInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
