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

from aionetbox.models.face import Face  # noqa: F401,E501
from aionetbox.models.nested_cluster import NestedCluster  # noqa: F401,E501
from aionetbox.models.nested_device import NestedDevice  # noqa: F401,E501
from aionetbox.models.nested_device_role import NestedDeviceRole  # noqa: F401,E501
from aionetbox.models.nested_device_type import NestedDeviceType  # noqa: F401,E501
from aionetbox.models.nested_ip_address import NestedIPAddress  # noqa: F401,E501
from aionetbox.models.nested_platform import NestedPlatform  # noqa: F401,E501
from aionetbox.models.nested_rack import NestedRack  # noqa: F401,E501
from aionetbox.models.nested_site import NestedSite  # noqa: F401,E501
from aionetbox.models.nested_tenant import NestedTenant  # noqa: F401,E501
from aionetbox.models.nested_virtual_chassis import NestedVirtualChassis  # noqa: F401,E501
from aionetbox.models.status import Status  # noqa: F401,E501


class Device(object):
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
        'display_name': 'str',
        'device_type': 'NestedDeviceType',
        'device_role': 'NestedDeviceRole',
        'tenant': 'NestedTenant',
        'platform': 'NestedPlatform',
        'serial': 'str',
        'asset_tag': 'str',
        'site': 'NestedSite',
        'rack': 'NestedRack',
        'position': 'int',
        'face': 'Face',
        'parent_device': 'NestedDevice',
        'status': 'Status',
        'primary_ip': 'NestedIPAddress',
        'primary_ip4': 'NestedIPAddress',
        'primary_ip6': 'NestedIPAddress',
        'cluster': 'NestedCluster',
        'virtual_chassis': 'NestedVirtualChassis',
        'vc_position': 'int',
        'vc_priority': 'int',
        'comments': 'str',
        'local_context_data': 'str',
        'tags': 'list[str]',
        'custom_fields': 'object',
        'created': 'date',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'display_name': 'display_name',
        'device_type': 'device_type',
        'device_role': 'device_role',
        'tenant': 'tenant',
        'platform': 'platform',
        'serial': 'serial',
        'asset_tag': 'asset_tag',
        'site': 'site',
        'rack': 'rack',
        'position': 'position',
        'face': 'face',
        'parent_device': 'parent_device',
        'status': 'status',
        'primary_ip': 'primary_ip',
        'primary_ip4': 'primary_ip4',
        'primary_ip6': 'primary_ip6',
        'cluster': 'cluster',
        'virtual_chassis': 'virtual_chassis',
        'vc_position': 'vc_position',
        'vc_priority': 'vc_priority',
        'comments': 'comments',
        'local_context_data': 'local_context_data',
        'tags': 'tags',
        'custom_fields': 'custom_fields',
        'created': 'created',
        'last_updated': 'last_updated'
    }

    def __init__(self, id=None, name=None, display_name=None, device_type=None, device_role=None, tenant=None, platform=None, serial=None, asset_tag=None, site=None, rack=None, position=None, face=None, parent_device=None, status=None, primary_ip=None, primary_ip4=None, primary_ip6=None, cluster=None, virtual_chassis=None, vc_position=None, vc_priority=None, comments=None, local_context_data=None, tags=None, custom_fields=None, created=None, last_updated=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._display_name = None
        self._device_type = None
        self._device_role = None
        self._tenant = None
        self._platform = None
        self._serial = None
        self._asset_tag = None
        self._site = None
        self._rack = None
        self._position = None
        self._face = None
        self._parent_device = None
        self._status = None
        self._primary_ip = None
        self._primary_ip4 = None
        self._primary_ip6 = None
        self._cluster = None
        self._virtual_chassis = None
        self._vc_position = None
        self._vc_priority = None
        self._comments = None
        self._local_context_data = None
        self._tags = None
        self._custom_fields = None
        self._created = None
        self._last_updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        self.device_type = device_type
        self.device_role = device_role
        if tenant is not None:
            self.tenant = tenant
        if platform is not None:
            self.platform = platform
        if serial is not None:
            self.serial = serial
        if asset_tag is not None:
            self.asset_tag = asset_tag
        self.site = site
        if rack is not None:
            self.rack = rack
        if position is not None:
            self.position = position
        if face is not None:
            self.face = face
        if parent_device is not None:
            self.parent_device = parent_device
        if status is not None:
            self.status = status
        if primary_ip is not None:
            self.primary_ip = primary_ip
        if primary_ip4 is not None:
            self.primary_ip4 = primary_ip4
        if primary_ip6 is not None:
            self.primary_ip6 = primary_ip6
        if cluster is not None:
            self.cluster = cluster
        if virtual_chassis is not None:
            self.virtual_chassis = virtual_chassis
        if vc_position is not None:
            self.vc_position = vc_position
        if vc_priority is not None:
            self.vc_priority = vc_priority
        if comments is not None:
            self.comments = comments
        if local_context_data is not None:
            self.local_context_data = local_context_data
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
        """Gets the id of this Device.  # noqa: E501


        :return: The id of this Device.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.


        :param id: The id of this Device.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Device.  # noqa: E501


        :return: The name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Device.


        :param name: The name of this Device.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this Device.  # noqa: E501


        :return: The display_name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Device.


        :param display_name: The display_name of this Device.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def device_type(self):
        """Gets the device_type of this Device.  # noqa: E501


        :return: The device_type of this Device.  # noqa: E501
        :rtype: NestedDeviceType
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this Device.


        :param device_type: The device_type of this Device.  # noqa: E501
        :type: NestedDeviceType
        """
        if device_type is None:
            raise ValueError("Invalid value for `device_type`, must not be `None`")  # noqa: E501

        self._device_type = device_type

    @property
    def device_role(self):
        """Gets the device_role of this Device.  # noqa: E501


        :return: The device_role of this Device.  # noqa: E501
        :rtype: NestedDeviceRole
        """
        return self._device_role

    @device_role.setter
    def device_role(self, device_role):
        """Sets the device_role of this Device.


        :param device_role: The device_role of this Device.  # noqa: E501
        :type: NestedDeviceRole
        """
        if device_role is None:
            raise ValueError("Invalid value for `device_role`, must not be `None`")  # noqa: E501

        self._device_role = device_role

    @property
    def tenant(self):
        """Gets the tenant of this Device.  # noqa: E501


        :return: The tenant of this Device.  # noqa: E501
        :rtype: NestedTenant
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this Device.


        :param tenant: The tenant of this Device.  # noqa: E501
        :type: NestedTenant
        """

        self._tenant = tenant

    @property
    def platform(self):
        """Gets the platform of this Device.  # noqa: E501


        :return: The platform of this Device.  # noqa: E501
        :rtype: NestedPlatform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this Device.


        :param platform: The platform of this Device.  # noqa: E501
        :type: NestedPlatform
        """

        self._platform = platform

    @property
    def serial(self):
        """Gets the serial of this Device.  # noqa: E501


        :return: The serial of this Device.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this Device.


        :param serial: The serial of this Device.  # noqa: E501
        :type: str
        """
        if serial is not None and len(serial) > 50:
            raise ValueError("Invalid value for `serial`, length must be less than or equal to `50`")  # noqa: E501

        self._serial = serial

    @property
    def asset_tag(self):
        """Gets the asset_tag of this Device.  # noqa: E501

        A unique tag used to identify this device  # noqa: E501

        :return: The asset_tag of this Device.  # noqa: E501
        :rtype: str
        """
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag):
        """Sets the asset_tag of this Device.

        A unique tag used to identify this device  # noqa: E501

        :param asset_tag: The asset_tag of this Device.  # noqa: E501
        :type: str
        """
        if asset_tag is not None and len(asset_tag) > 50:
            raise ValueError("Invalid value for `asset_tag`, length must be less than or equal to `50`")  # noqa: E501

        self._asset_tag = asset_tag

    @property
    def site(self):
        """Gets the site of this Device.  # noqa: E501


        :return: The site of this Device.  # noqa: E501
        :rtype: NestedSite
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this Device.


        :param site: The site of this Device.  # noqa: E501
        :type: NestedSite
        """
        if site is None:
            raise ValueError("Invalid value for `site`, must not be `None`")  # noqa: E501

        self._site = site

    @property
    def rack(self):
        """Gets the rack of this Device.  # noqa: E501


        :return: The rack of this Device.  # noqa: E501
        :rtype: NestedRack
        """
        return self._rack

    @rack.setter
    def rack(self, rack):
        """Sets the rack of this Device.


        :param rack: The rack of this Device.  # noqa: E501
        :type: NestedRack
        """

        self._rack = rack

    @property
    def position(self):
        """Gets the position of this Device.  # noqa: E501

        The lowest-numbered unit occupied by the device  # noqa: E501

        :return: The position of this Device.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Device.

        The lowest-numbered unit occupied by the device  # noqa: E501

        :param position: The position of this Device.  # noqa: E501
        :type: int
        """
        if position is not None and position > 32767:  # noqa: E501
            raise ValueError("Invalid value for `position`, must be a value less than or equal to `32767`")  # noqa: E501
        if position is not None and position < 1:  # noqa: E501
            raise ValueError("Invalid value for `position`, must be a value greater than or equal to `1`")  # noqa: E501

        self._position = position

    @property
    def face(self):
        """Gets the face of this Device.  # noqa: E501


        :return: The face of this Device.  # noqa: E501
        :rtype: Face
        """
        return self._face

    @face.setter
    def face(self, face):
        """Sets the face of this Device.


        :param face: The face of this Device.  # noqa: E501
        :type: Face
        """

        self._face = face

    @property
    def parent_device(self):
        """Gets the parent_device of this Device.  # noqa: E501


        :return: The parent_device of this Device.  # noqa: E501
        :rtype: NestedDevice
        """
        return self._parent_device

    @parent_device.setter
    def parent_device(self, parent_device):
        """Sets the parent_device of this Device.


        :param parent_device: The parent_device of this Device.  # noqa: E501
        :type: NestedDevice
        """

        self._parent_device = parent_device

    @property
    def status(self):
        """Gets the status of this Device.  # noqa: E501


        :return: The status of this Device.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Device.


        :param status: The status of this Device.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def primary_ip(self):
        """Gets the primary_ip of this Device.  # noqa: E501


        :return: The primary_ip of this Device.  # noqa: E501
        :rtype: NestedIPAddress
        """
        return self._primary_ip

    @primary_ip.setter
    def primary_ip(self, primary_ip):
        """Sets the primary_ip of this Device.


        :param primary_ip: The primary_ip of this Device.  # noqa: E501
        :type: NestedIPAddress
        """

        self._primary_ip = primary_ip

    @property
    def primary_ip4(self):
        """Gets the primary_ip4 of this Device.  # noqa: E501


        :return: The primary_ip4 of this Device.  # noqa: E501
        :rtype: NestedIPAddress
        """
        return self._primary_ip4

    @primary_ip4.setter
    def primary_ip4(self, primary_ip4):
        """Sets the primary_ip4 of this Device.


        :param primary_ip4: The primary_ip4 of this Device.  # noqa: E501
        :type: NestedIPAddress
        """

        self._primary_ip4 = primary_ip4

    @property
    def primary_ip6(self):
        """Gets the primary_ip6 of this Device.  # noqa: E501


        :return: The primary_ip6 of this Device.  # noqa: E501
        :rtype: NestedIPAddress
        """
        return self._primary_ip6

    @primary_ip6.setter
    def primary_ip6(self, primary_ip6):
        """Sets the primary_ip6 of this Device.


        :param primary_ip6: The primary_ip6 of this Device.  # noqa: E501
        :type: NestedIPAddress
        """

        self._primary_ip6 = primary_ip6

    @property
    def cluster(self):
        """Gets the cluster of this Device.  # noqa: E501


        :return: The cluster of this Device.  # noqa: E501
        :rtype: NestedCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this Device.


        :param cluster: The cluster of this Device.  # noqa: E501
        :type: NestedCluster
        """

        self._cluster = cluster

    @property
    def virtual_chassis(self):
        """Gets the virtual_chassis of this Device.  # noqa: E501


        :return: The virtual_chassis of this Device.  # noqa: E501
        :rtype: NestedVirtualChassis
        """
        return self._virtual_chassis

    @virtual_chassis.setter
    def virtual_chassis(self, virtual_chassis):
        """Sets the virtual_chassis of this Device.


        :param virtual_chassis: The virtual_chassis of this Device.  # noqa: E501
        :type: NestedVirtualChassis
        """

        self._virtual_chassis = virtual_chassis

    @property
    def vc_position(self):
        """Gets the vc_position of this Device.  # noqa: E501


        :return: The vc_position of this Device.  # noqa: E501
        :rtype: int
        """
        return self._vc_position

    @vc_position.setter
    def vc_position(self, vc_position):
        """Sets the vc_position of this Device.


        :param vc_position: The vc_position of this Device.  # noqa: E501
        :type: int
        """
        if vc_position is not None and vc_position > 255:  # noqa: E501
            raise ValueError("Invalid value for `vc_position`, must be a value less than or equal to `255`")  # noqa: E501
        if vc_position is not None and vc_position < 0:  # noqa: E501
            raise ValueError("Invalid value for `vc_position`, must be a value greater than or equal to `0`")  # noqa: E501

        self._vc_position = vc_position

    @property
    def vc_priority(self):
        """Gets the vc_priority of this Device.  # noqa: E501


        :return: The vc_priority of this Device.  # noqa: E501
        :rtype: int
        """
        return self._vc_priority

    @vc_priority.setter
    def vc_priority(self, vc_priority):
        """Sets the vc_priority of this Device.


        :param vc_priority: The vc_priority of this Device.  # noqa: E501
        :type: int
        """
        if vc_priority is not None and vc_priority > 255:  # noqa: E501
            raise ValueError("Invalid value for `vc_priority`, must be a value less than or equal to `255`")  # noqa: E501
        if vc_priority is not None and vc_priority < 0:  # noqa: E501
            raise ValueError("Invalid value for `vc_priority`, must be a value greater than or equal to `0`")  # noqa: E501

        self._vc_priority = vc_priority

    @property
    def comments(self):
        """Gets the comments of this Device.  # noqa: E501


        :return: The comments of this Device.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Device.


        :param comments: The comments of this Device.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def local_context_data(self):
        """Gets the local_context_data of this Device.  # noqa: E501


        :return: The local_context_data of this Device.  # noqa: E501
        :rtype: str
        """
        return self._local_context_data

    @local_context_data.setter
    def local_context_data(self, local_context_data):
        """Sets the local_context_data of this Device.


        :param local_context_data: The local_context_data of this Device.  # noqa: E501
        :type: str
        """

        self._local_context_data = local_context_data

    @property
    def tags(self):
        """Gets the tags of this Device.  # noqa: E501


        :return: The tags of this Device.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Device.


        :param tags: The tags of this Device.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Device.  # noqa: E501


        :return: The custom_fields of this Device.  # noqa: E501
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Device.


        :param custom_fields: The custom_fields of this Device.  # noqa: E501
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def created(self):
        """Gets the created of this Device.  # noqa: E501


        :return: The created of this Device.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Device.


        :param created: The created of this Device.  # noqa: E501
        :type: date
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this Device.  # noqa: E501


        :return: The last_updated of this Device.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this Device.


        :param last_updated: The last_updated of this Device.  # noqa: E501
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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
