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


class NestedVLAN(object):
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
        'vid': 'int',
        'name': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'vid': 'vid',
        'name': 'name',
        'display_name': 'display_name'
    }

    def __init__(self, id=None, url=None, vid=None, name=None, display_name=None):  # noqa: E501
        """NestedVLAN - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._url = None
        self._vid = None
        self._name = None
        self._display_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        self.vid = vid
        self.name = name
        if display_name is not None:
            self.display_name = display_name

    @property
    def id(self):
        """Gets the id of this NestedVLAN.  # noqa: E501


        :return: The id of this NestedVLAN.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NestedVLAN.


        :param id: The id of this NestedVLAN.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this NestedVLAN.  # noqa: E501


        :return: The url of this NestedVLAN.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NestedVLAN.


        :param url: The url of this NestedVLAN.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def vid(self):
        """Gets the vid of this NestedVLAN.  # noqa: E501


        :return: The vid of this NestedVLAN.  # noqa: E501
        :rtype: int
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """Sets the vid of this NestedVLAN.


        :param vid: The vid of this NestedVLAN.  # noqa: E501
        :type: int
        """
        if vid is None:
            raise ValueError("Invalid value for `vid`, must not be `None`")  # noqa: E501
        if vid is not None and vid > 4094:  # noqa: E501
            raise ValueError("Invalid value for `vid`, must be a value less than or equal to `4094`")  # noqa: E501
        if vid is not None and vid < 1:  # noqa: E501
            raise ValueError("Invalid value for `vid`, must be a value greater than or equal to `1`")  # noqa: E501

        self._vid = vid

    @property
    def name(self):
        """Gets the name of this NestedVLAN.  # noqa: E501


        :return: The name of this NestedVLAN.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NestedVLAN.


        :param name: The name of this NestedVLAN.  # noqa: E501
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
    def display_name(self):
        """Gets the display_name of this NestedVLAN.  # noqa: E501


        :return: The display_name of this NestedVLAN.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this NestedVLAN.


        :param display_name: The display_name of this NestedVLAN.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

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
        if issubclass(NestedVLAN, dict):
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
        if not isinstance(other, NestedVLAN):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
