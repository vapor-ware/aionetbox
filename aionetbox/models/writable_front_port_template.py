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


class WritableFrontPortTemplate(object):
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
        'device_type': 'int',
        'name': 'str',
        'type': 'int',
        'rear_port': 'int',
        'rear_port_position': 'int'
    }

    attribute_map = {
        'id': 'id',
        'device_type': 'device_type',
        'name': 'name',
        'type': 'type',
        'rear_port': 'rear_port',
        'rear_port_position': 'rear_port_position'
    }

    def __init__(self, id=None, device_type=None, name=None, type=None, rear_port=None, rear_port_position=None):  # noqa: E501
        """WritableFrontPortTemplate - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._device_type = None
        self._name = None
        self._type = None
        self._rear_port = None
        self._rear_port_position = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.device_type = device_type
        self.name = name
        self.type = type
        self.rear_port = rear_port
        if rear_port_position is not None:
            self.rear_port_position = rear_port_position

    @property
    def id(self):
        """Gets the id of this WritableFrontPortTemplate.  # noqa: E501


        :return: The id of this WritableFrontPortTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WritableFrontPortTemplate.


        :param id: The id of this WritableFrontPortTemplate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def device_type(self):
        """Gets the device_type of this WritableFrontPortTemplate.  # noqa: E501


        :return: The device_type of this WritableFrontPortTemplate.  # noqa: E501
        :rtype: int
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this WritableFrontPortTemplate.


        :param device_type: The device_type of this WritableFrontPortTemplate.  # noqa: E501
        :type: int
        """
        if device_type is None:
            raise ValueError("Invalid value for `device_type`, must not be `None`")  # noqa: E501

        self._device_type = device_type

    @property
    def name(self):
        """Gets the name of this WritableFrontPortTemplate.  # noqa: E501


        :return: The name of this WritableFrontPortTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WritableFrontPortTemplate.


        :param name: The name of this WritableFrontPortTemplate.  # noqa: E501
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
        """Gets the type of this WritableFrontPortTemplate.  # noqa: E501


        :return: The type of this WritableFrontPortTemplate.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WritableFrontPortTemplate.


        :param type: The type of this WritableFrontPortTemplate.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def rear_port(self):
        """Gets the rear_port of this WritableFrontPortTemplate.  # noqa: E501


        :return: The rear_port of this WritableFrontPortTemplate.  # noqa: E501
        :rtype: int
        """
        return self._rear_port

    @rear_port.setter
    def rear_port(self, rear_port):
        """Sets the rear_port of this WritableFrontPortTemplate.


        :param rear_port: The rear_port of this WritableFrontPortTemplate.  # noqa: E501
        :type: int
        """
        if rear_port is None:
            raise ValueError("Invalid value for `rear_port`, must not be `None`")  # noqa: E501

        self._rear_port = rear_port

    @property
    def rear_port_position(self):
        """Gets the rear_port_position of this WritableFrontPortTemplate.  # noqa: E501


        :return: The rear_port_position of this WritableFrontPortTemplate.  # noqa: E501
        :rtype: int
        """
        return self._rear_port_position

    @rear_port_position.setter
    def rear_port_position(self, rear_port_position):
        """Sets the rear_port_position of this WritableFrontPortTemplate.


        :param rear_port_position: The rear_port_position of this WritableFrontPortTemplate.  # noqa: E501
        :type: int
        """
        if rear_port_position is not None and rear_port_position > 64:  # noqa: E501
            raise ValueError("Invalid value for `rear_port_position`, must be a value less than or equal to `64`")  # noqa: E501
        if rear_port_position is not None and rear_port_position < 1:  # noqa: E501
            raise ValueError("Invalid value for `rear_port_position`, must be a value greater than or equal to `1`")  # noqa: E501

        self._rear_port_position = rear_port_position

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
        if issubclass(WritableFrontPortTemplate, dict):
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
        if not isinstance(other, WritableFrontPortTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
