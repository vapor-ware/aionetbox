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


class NestedCircuit(object):
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
        'cid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'cid': 'cid'
    }

    def __init__(self, id=None, url=None, cid=None):  # noqa: E501
        """NestedCircuit - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._url = None
        self._cid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        self.cid = cid

    @property
    def id(self):
        """Gets the id of this NestedCircuit.  # noqa: E501


        :return: The id of this NestedCircuit.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NestedCircuit.


        :param id: The id of this NestedCircuit.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this NestedCircuit.  # noqa: E501


        :return: The url of this NestedCircuit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NestedCircuit.


        :param url: The url of this NestedCircuit.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def cid(self):
        """Gets the cid of this NestedCircuit.  # noqa: E501


        :return: The cid of this NestedCircuit.  # noqa: E501
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this NestedCircuit.


        :param cid: The cid of this NestedCircuit.  # noqa: E501
        :type: str
        """
        if cid is None:
            raise ValueError("Invalid value for `cid`, must not be `None`")  # noqa: E501
        if cid is not None and len(cid) > 50:
            raise ValueError("Invalid value for `cid`, length must be less than or equal to `50`")  # noqa: E501
        if cid is not None and len(cid) < 1:
            raise ValueError("Invalid value for `cid`, length must be greater than or equal to `1`")  # noqa: E501

        self._cid = cid

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
        if issubclass(NestedCircuit, dict):
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
        if not isinstance(other, NestedCircuit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
