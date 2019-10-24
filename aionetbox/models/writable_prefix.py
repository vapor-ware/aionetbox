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


class WritablePrefix(object):
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
        'family': 'int',
        'prefix': 'str',
        'site': 'int',
        'vrf': 'int',
        'tenant': 'int',
        'vlan': 'int',
        'status': 'int',
        'role': 'int',
        'is_pool': 'bool',
        'description': 'str',
        'tags': 'list[str]',
        'custom_fields': 'object',
        'created': 'date',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'family': 'family',
        'prefix': 'prefix',
        'site': 'site',
        'vrf': 'vrf',
        'tenant': 'tenant',
        'vlan': 'vlan',
        'status': 'status',
        'role': 'role',
        'is_pool': 'is_pool',
        'description': 'description',
        'tags': 'tags',
        'custom_fields': 'custom_fields',
        'created': 'created',
        'last_updated': 'last_updated'
    }

    def __init__(self, id=None, family=None, prefix=None, site=None, vrf=None, tenant=None, vlan=None, status=None, role=None, is_pool=None, description=None, tags=None, custom_fields=None, created=None, last_updated=None):  # noqa: E501
        """WritablePrefix - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._family = None
        self._prefix = None
        self._site = None
        self._vrf = None
        self._tenant = None
        self._vlan = None
        self._status = None
        self._role = None
        self._is_pool = None
        self._description = None
        self._tags = None
        self._custom_fields = None
        self._created = None
        self._last_updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if family is not None:
            self.family = family
        self.prefix = prefix
        if site is not None:
            self.site = site
        if vrf is not None:
            self.vrf = vrf
        if tenant is not None:
            self.tenant = tenant
        if vlan is not None:
            self.vlan = vlan
        if status is not None:
            self.status = status
        if role is not None:
            self.role = role
        if is_pool is not None:
            self.is_pool = is_pool
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if created is not None:
            self.created = created
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def id(self):
        """Gets the id of this WritablePrefix.  # noqa: E501


        :return: The id of this WritablePrefix.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WritablePrefix.


        :param id: The id of this WritablePrefix.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def family(self):
        """Gets the family of this WritablePrefix.  # noqa: E501


        :return: The family of this WritablePrefix.  # noqa: E501
        :rtype: int
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this WritablePrefix.


        :param family: The family of this WritablePrefix.  # noqa: E501
        :type: int
        """

        self._family = family

    @property
    def prefix(self):
        """Gets the prefix of this WritablePrefix.  # noqa: E501

        IPv4 or IPv6 network with mask  # noqa: E501

        :return: The prefix of this WritablePrefix.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this WritablePrefix.

        IPv4 or IPv6 network with mask  # noqa: E501

        :param prefix: The prefix of this WritablePrefix.  # noqa: E501
        :type: str
        """
        if prefix is None:
            raise ValueError("Invalid value for `prefix`, must not be `None`")  # noqa: E501

        self._prefix = prefix

    @property
    def site(self):
        """Gets the site of this WritablePrefix.  # noqa: E501


        :return: The site of this WritablePrefix.  # noqa: E501
        :rtype: int
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this WritablePrefix.


        :param site: The site of this WritablePrefix.  # noqa: E501
        :type: int
        """

        self._site = site

    @property
    def vrf(self):
        """Gets the vrf of this WritablePrefix.  # noqa: E501


        :return: The vrf of this WritablePrefix.  # noqa: E501
        :rtype: int
        """
        return self._vrf

    @vrf.setter
    def vrf(self, vrf):
        """Sets the vrf of this WritablePrefix.


        :param vrf: The vrf of this WritablePrefix.  # noqa: E501
        :type: int
        """

        self._vrf = vrf

    @property
    def tenant(self):
        """Gets the tenant of this WritablePrefix.  # noqa: E501


        :return: The tenant of this WritablePrefix.  # noqa: E501
        :rtype: int
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this WritablePrefix.


        :param tenant: The tenant of this WritablePrefix.  # noqa: E501
        :type: int
        """

        self._tenant = tenant

    @property
    def vlan(self):
        """Gets the vlan of this WritablePrefix.  # noqa: E501


        :return: The vlan of this WritablePrefix.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this WritablePrefix.


        :param vlan: The vlan of this WritablePrefix.  # noqa: E501
        :type: int
        """

        self._vlan = vlan

    @property
    def status(self):
        """Gets the status of this WritablePrefix.  # noqa: E501

        Operational status of this prefix  # noqa: E501

        :return: The status of this WritablePrefix.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WritablePrefix.

        Operational status of this prefix  # noqa: E501

        :param status: The status of this WritablePrefix.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def role(self):
        """Gets the role of this WritablePrefix.  # noqa: E501

        The primary function of this prefix  # noqa: E501

        :return: The role of this WritablePrefix.  # noqa: E501
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this WritablePrefix.

        The primary function of this prefix  # noqa: E501

        :param role: The role of this WritablePrefix.  # noqa: E501
        :type: int
        """

        self._role = role

    @property
    def is_pool(self):
        """Gets the is_pool of this WritablePrefix.  # noqa: E501

        All IP addresses within this prefix are considered usable  # noqa: E501

        :return: The is_pool of this WritablePrefix.  # noqa: E501
        :rtype: bool
        """
        return self._is_pool

    @is_pool.setter
    def is_pool(self, is_pool):
        """Sets the is_pool of this WritablePrefix.

        All IP addresses within this prefix are considered usable  # noqa: E501

        :param is_pool: The is_pool of this WritablePrefix.  # noqa: E501
        :type: bool
        """

        self._is_pool = is_pool

    @property
    def description(self):
        """Gets the description of this WritablePrefix.  # noqa: E501


        :return: The description of this WritablePrefix.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WritablePrefix.


        :param description: The description of this WritablePrefix.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this WritablePrefix.  # noqa: E501


        :return: The tags of this WritablePrefix.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WritablePrefix.


        :param tags: The tags of this WritablePrefix.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def custom_fields(self):
        """Gets the custom_fields of this WritablePrefix.  # noqa: E501


        :return: The custom_fields of this WritablePrefix.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this WritablePrefix.


        :param custom_fields: The custom_fields of this WritablePrefix.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def created(self):
        """Gets the created of this WritablePrefix.  # noqa: E501


        :return: The created of this WritablePrefix.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this WritablePrefix.


        :param created: The created of this WritablePrefix.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this WritablePrefix.  # noqa: E501


        :return: The last_updated of this WritablePrefix.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this WritablePrefix.


        :param last_updated: The last_updated of this WritablePrefix.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

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
        if issubclass(WritablePrefix, dict):
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
        if not isinstance(other, WritablePrefix):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
