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


class Role(object):
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
        'name': 'str',
        'slug': 'str',
        'weight': 'int',
        'prefix_count': 'int',
        'vlan_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'weight': 'weight',
        'prefix_count': 'prefix_count',
        'vlan_count': 'vlan_count'
    }

    def __init__(self, id=None, name=None, slug=None, weight=None, prefix_count=None, vlan_count=None):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._slug = None
        self._weight = None
        self._prefix_count = None
        self._vlan_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.slug = slug
        if weight is not None:
            self.weight = weight
        if prefix_count is not None:
            self.prefix_count = prefix_count
        if vlan_count is not None:
            self.vlan_count = vlan_count

    @property
    def id(self):
        """Gets the id of this Role.  # noqa: E501


        :return: The id of this Role.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Role.


        :param id: The id of this Role.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Role.  # noqa: E501


        :return: The name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Role.


        :param name: The name of this Role.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Role.  # noqa: E501


        :return: The slug of this Role.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Role.


        :param slug: The slug of this Role.  # noqa: E501
        :type: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501
        if slug is not None and len(slug) > 50:
            raise ValueError("Invalid value for `slug`, length must be less than or equal to `50`")  # noqa: E501
        if slug is not None and len(slug) < 1:
            raise ValueError("Invalid value for `slug`, length must be greater than or equal to `1`")  # noqa: E501
        if slug is not None and not re.search(r'^[-a-zA-Z0-9_]+$', slug):  # noqa: E501
            raise ValueError(r"Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._slug = slug

    @property
    def weight(self):
        """Gets the weight of this Role.  # noqa: E501


        :return: The weight of this Role.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Role.


        :param weight: The weight of this Role.  # noqa: E501
        :type: int
        """
        if weight is not None and weight > 32767:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must be a value less than or equal to `32767`")  # noqa: E501
        if weight is not None and weight < 0:  # noqa: E501
            raise ValueError("Invalid value for `weight`, must be a value greater than or equal to `0`")  # noqa: E501

        self._weight = weight

    @property
    def prefix_count(self):
        """Gets the prefix_count of this Role.  # noqa: E501


        :return: The prefix_count of this Role.  # noqa: E501
        :rtype: int
        """
        return self._prefix_count

    @prefix_count.setter
    def prefix_count(self, prefix_count):
        """Sets the prefix_count of this Role.


        :param prefix_count: The prefix_count of this Role.  # noqa: E501
        :type: int
        """

        self._prefix_count = prefix_count

    @property
    def vlan_count(self):
        """Gets the vlan_count of this Role.  # noqa: E501


        :return: The vlan_count of this Role.  # noqa: E501
        :rtype: int
        """
        return self._vlan_count

    @vlan_count.setter
    def vlan_count(self, vlan_count):
        """Sets the vlan_count of this Role.


        :param vlan_count: The vlan_count of this Role.  # noqa: E501
        :type: int
        """

        self._vlan_count = vlan_count

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
        if issubclass(Role, dict):
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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
