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
from aionetbox.models.nested_device import NestedDevice  # noqa: F401,E501


class NestedInterface(object):
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
        'url': 'str',
        'device': 'NestedDevice',
        'name': 'str',
        'cable': 'int',
        'connection_status': 'ConnectionStatus'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'device': 'device',
        'name': 'name',
        'cable': 'cable',
        'connection_status': 'connection_status'
    }

    def __init__(self, id=None, url=None, device=None, name=None, cable=None, connection_status=None):  # noqa: E501
        """NestedInterface - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._url = None
        self._device = None
        self._name = None
        self._cable = None
        self._connection_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if device is not None:
            self.device = device
        self.name = name
        if cable is not None:
            self.cable = cable
        if connection_status is not None:
            self.connection_status = connection_status

    @property
    def id(self):
        """Gets the id of this NestedInterface.  # noqa: E501


        :return: The id of this NestedInterface.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NestedInterface.


        :param id: The id of this NestedInterface.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this NestedInterface.  # noqa: E501


        :return: The url of this NestedInterface.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NestedInterface.


        :param url: The url of this NestedInterface.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def device(self):
        """Gets the device of this NestedInterface.  # noqa: E501


        :return: The device of this NestedInterface.  # noqa: E501
        :rtype: NestedDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this NestedInterface.


        :param device: The device of this NestedInterface.  # noqa: E501
        :type: NestedDevice
        """

        self._device = device

    @property
    def name(self):
        """Gets the name of this NestedInterface.  # noqa: E501


        :return: The name of this NestedInterface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NestedInterface.


        :param name: The name of this NestedInterface.  # noqa: E501
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
    def cable(self):
        """Gets the cable of this NestedInterface.  # noqa: E501


        :return: The cable of this NestedInterface.  # noqa: E501
        :rtype: int
        """
        return self._cable

    @cable.setter
    def cable(self, cable):
        """Sets the cable of this NestedInterface.


        :param cable: The cable of this NestedInterface.  # noqa: E501
        :type: int
        """

        self._cable = cable

    @property
    def connection_status(self):
        """Gets the connection_status of this NestedInterface.  # noqa: E501


        :return: The connection_status of this NestedInterface.  # noqa: E501
        :rtype: ConnectionStatus
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this NestedInterface.


        :param connection_status: The connection_status of this NestedInterface.  # noqa: E501
        :type: ConnectionStatus
        """

        self._connection_status = connection_status

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
        if issubclass(NestedInterface, dict):
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
        if not isinstance(other, NestedInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
