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


class Manufacturer(object):
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
        'devicetype_count': 'int',
        'inventoryitem_count': 'int',
        'platform_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'devicetype_count': 'devicetype_count',
        'inventoryitem_count': 'inventoryitem_count',
        'platform_count': 'platform_count'
    }

    def __init__(self, id=None, name=None, slug=None, devicetype_count=None, inventoryitem_count=None, platform_count=None):  # noqa: E501
        """Manufacturer - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._slug = None
        self._devicetype_count = None
        self._inventoryitem_count = None
        self._platform_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.slug = slug
        if devicetype_count is not None:
            self.devicetype_count = devicetype_count
        if inventoryitem_count is not None:
            self.inventoryitem_count = inventoryitem_count
        if platform_count is not None:
            self.platform_count = platform_count

    @property
    def id(self):
        """Gets the id of this Manufacturer.  # noqa: E501


        :return: The id of this Manufacturer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Manufacturer.


        :param id: The id of this Manufacturer.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Manufacturer.  # noqa: E501


        :return: The name of this Manufacturer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Manufacturer.


        :param name: The name of this Manufacturer.  # noqa: E501
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
        """Gets the slug of this Manufacturer.  # noqa: E501


        :return: The slug of this Manufacturer.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Manufacturer.


        :param slug: The slug of this Manufacturer.  # noqa: E501
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
    def devicetype_count(self):
        """Gets the devicetype_count of this Manufacturer.  # noqa: E501


        :return: The devicetype_count of this Manufacturer.  # noqa: E501
        :rtype: int
        """
        return self._devicetype_count

    @devicetype_count.setter
    def devicetype_count(self, devicetype_count):
        """Sets the devicetype_count of this Manufacturer.


        :param devicetype_count: The devicetype_count of this Manufacturer.  # noqa: E501
        :type: int
        """

        self._devicetype_count = devicetype_count

    @property
    def inventoryitem_count(self):
        """Gets the inventoryitem_count of this Manufacturer.  # noqa: E501


        :return: The inventoryitem_count of this Manufacturer.  # noqa: E501
        :rtype: int
        """
        return self._inventoryitem_count

    @inventoryitem_count.setter
    def inventoryitem_count(self, inventoryitem_count):
        """Sets the inventoryitem_count of this Manufacturer.


        :param inventoryitem_count: The inventoryitem_count of this Manufacturer.  # noqa: E501
        :type: int
        """

        self._inventoryitem_count = inventoryitem_count

    @property
    def platform_count(self):
        """Gets the platform_count of this Manufacturer.  # noqa: E501


        :return: The platform_count of this Manufacturer.  # noqa: E501
        :rtype: int
        """
        return self._platform_count

    @platform_count.setter
    def platform_count(self, platform_count):
        """Sets the platform_count of this Manufacturer.


        :param platform_count: The platform_count of this Manufacturer.  # noqa: E501
        :type: int
        """

        self._platform_count = platform_count

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
        if issubclass(Manufacturer, dict):
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
        if not isinstance(other, Manufacturer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
