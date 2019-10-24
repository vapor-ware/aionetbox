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


class NestedSecretRole(object):
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
        'name': 'str',
        'slug': 'str',
        'secret_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'name': 'name',
        'slug': 'slug',
        'secret_count': 'secret_count'
    }

    def __init__(self, id=None, url=None, name=None, slug=None, secret_count=None):  # noqa: E501
        """NestedSecretRole - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._url = None
        self._name = None
        self._slug = None
        self._secret_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        self.name = name
        self.slug = slug
        if secret_count is not None:
            self.secret_count = secret_count

    @property
    def id(self):
        """Gets the id of this NestedSecretRole.  # noqa: E501


        :return: The id of this NestedSecretRole.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NestedSecretRole.


        :param id: The id of this NestedSecretRole.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this NestedSecretRole.  # noqa: E501


        :return: The url of this NestedSecretRole.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NestedSecretRole.


        :param url: The url of this NestedSecretRole.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this NestedSecretRole.  # noqa: E501


        :return: The name of this NestedSecretRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NestedSecretRole.


        :param name: The name of this NestedSecretRole.  # noqa: E501
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
        """Gets the slug of this NestedSecretRole.  # noqa: E501


        :return: The slug of this NestedSecretRole.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this NestedSecretRole.


        :param slug: The slug of this NestedSecretRole.  # noqa: E501
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
    def secret_count(self):
        """Gets the secret_count of this NestedSecretRole.  # noqa: E501


        :return: The secret_count of this NestedSecretRole.  # noqa: E501
        :rtype: int
        """
        return self._secret_count

    @secret_count.setter
    def secret_count(self, secret_count):
        """Sets the secret_count of this NestedSecretRole.


        :param secret_count: The secret_count of this NestedSecretRole.  # noqa: E501
        :type: int
        """

        self._secret_count = secret_count

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
        if issubclass(NestedSecretRole, dict):
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
        if not isinstance(other, NestedSecretRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
