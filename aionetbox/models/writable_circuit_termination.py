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

from aionetbox.models.nested_cable import NestedCable  # noqa: F401,E501


class WritableCircuitTermination(object):
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
        'circuit': 'int',
        'term_side': 'str',
        'site': 'int',
        'port_speed': 'int',
        'upstream_speed': 'int',
        'xconnect_id': 'str',
        'pp_info': 'str',
        'description': 'str',
        'connected_endpoint_type': 'str',
        'connected_endpoint': 'dict(str, str)',
        'connection_status': 'bool',
        'cable': 'NestedCable'
    }

    attribute_map = {
        'id': 'id',
        'circuit': 'circuit',
        'term_side': 'term_side',
        'site': 'site',
        'port_speed': 'port_speed',
        'upstream_speed': 'upstream_speed',
        'xconnect_id': 'xconnect_id',
        'pp_info': 'pp_info',
        'description': 'description',
        'connected_endpoint_type': 'connected_endpoint_type',
        'connected_endpoint': 'connected_endpoint',
        'connection_status': 'connection_status',
        'cable': 'cable'
    }

    def __init__(self, id=None, circuit=None, term_side=None, site=None, port_speed=None, upstream_speed=None, xconnect_id=None, pp_info=None, description=None, connected_endpoint_type=None, connected_endpoint=None, connection_status=None, cable=None):  # noqa: E501
        """WritableCircuitTermination - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._circuit = None
        self._term_side = None
        self._site = None
        self._port_speed = None
        self._upstream_speed = None
        self._xconnect_id = None
        self._pp_info = None
        self._description = None
        self._connected_endpoint_type = None
        self._connected_endpoint = None
        self._connection_status = None
        self._cable = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.circuit = circuit
        self.term_side = term_side
        self.site = site
        self.port_speed = port_speed
        if upstream_speed is not None:
            self.upstream_speed = upstream_speed
        if xconnect_id is not None:
            self.xconnect_id = xconnect_id
        if pp_info is not None:
            self.pp_info = pp_info
        if description is not None:
            self.description = description
        if connected_endpoint_type is not None:
            self.connected_endpoint_type = connected_endpoint_type
        if connected_endpoint is not None:
            self.connected_endpoint = connected_endpoint
        if connection_status is not None:
            self.connection_status = connection_status
        if cable is not None:
            self.cable = cable

    @property
    def id(self):
        """Gets the id of this WritableCircuitTermination.  # noqa: E501


        :return: The id of this WritableCircuitTermination.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WritableCircuitTermination.


        :param id: The id of this WritableCircuitTermination.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def circuit(self):
        """Gets the circuit of this WritableCircuitTermination.  # noqa: E501


        :return: The circuit of this WritableCircuitTermination.  # noqa: E501
        :rtype: int
        """
        return self._circuit

    @circuit.setter
    def circuit(self, circuit):
        """Sets the circuit of this WritableCircuitTermination.


        :param circuit: The circuit of this WritableCircuitTermination.  # noqa: E501
        :type: int
        """
        if circuit is None:
            raise ValueError("Invalid value for `circuit`, must not be `None`")  # noqa: E501

        self._circuit = circuit

    @property
    def term_side(self):
        """Gets the term_side of this WritableCircuitTermination.  # noqa: E501


        :return: The term_side of this WritableCircuitTermination.  # noqa: E501
        :rtype: str
        """
        return self._term_side

    @term_side.setter
    def term_side(self, term_side):
        """Sets the term_side of this WritableCircuitTermination.


        :param term_side: The term_side of this WritableCircuitTermination.  # noqa: E501
        :type: str
        """
        if term_side is None:
            raise ValueError("Invalid value for `term_side`, must not be `None`")  # noqa: E501
        allowed_values = ["A", "Z"]  # noqa: E501
        if term_side not in allowed_values:
            raise ValueError(
                "Invalid value for `term_side` ({0}), must be one of {1}"  # noqa: E501
                .format(term_side, allowed_values)
            )

        self._term_side = term_side

    @property
    def site(self):
        """Gets the site of this WritableCircuitTermination.  # noqa: E501


        :return: The site of this WritableCircuitTermination.  # noqa: E501
        :rtype: int
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this WritableCircuitTermination.


        :param site: The site of this WritableCircuitTermination.  # noqa: E501
        :type: int
        """
        if site is None:
            raise ValueError("Invalid value for `site`, must not be `None`")  # noqa: E501

        self._site = site

    @property
    def port_speed(self):
        """Gets the port_speed of this WritableCircuitTermination.  # noqa: E501


        :return: The port_speed of this WritableCircuitTermination.  # noqa: E501
        :rtype: int
        """
        return self._port_speed

    @port_speed.setter
    def port_speed(self, port_speed):
        """Sets the port_speed of this WritableCircuitTermination.


        :param port_speed: The port_speed of this WritableCircuitTermination.  # noqa: E501
        :type: int
        """
        if port_speed is None:
            raise ValueError("Invalid value for `port_speed`, must not be `None`")  # noqa: E501
        if port_speed is not None and port_speed > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `port_speed`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if port_speed is not None and port_speed < 0:  # noqa: E501
            raise ValueError("Invalid value for `port_speed`, must be a value greater than or equal to `0`")  # noqa: E501

        self._port_speed = port_speed

    @property
    def upstream_speed(self):
        """Gets the upstream_speed of this WritableCircuitTermination.  # noqa: E501

        Upstream speed, if different from port speed  # noqa: E501

        :return: The upstream_speed of this WritableCircuitTermination.  # noqa: E501
        :rtype: int
        """
        return self._upstream_speed

    @upstream_speed.setter
    def upstream_speed(self, upstream_speed):
        """Sets the upstream_speed of this WritableCircuitTermination.

        Upstream speed, if different from port speed  # noqa: E501

        :param upstream_speed: The upstream_speed of this WritableCircuitTermination.  # noqa: E501
        :type: int
        """
        if upstream_speed is not None and upstream_speed > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `upstream_speed`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if upstream_speed is not None and upstream_speed < 0:  # noqa: E501
            raise ValueError("Invalid value for `upstream_speed`, must be a value greater than or equal to `0`")  # noqa: E501

        self._upstream_speed = upstream_speed

    @property
    def xconnect_id(self):
        """Gets the xconnect_id of this WritableCircuitTermination.  # noqa: E501


        :return: The xconnect_id of this WritableCircuitTermination.  # noqa: E501
        :rtype: str
        """
        return self._xconnect_id

    @xconnect_id.setter
    def xconnect_id(self, xconnect_id):
        """Sets the xconnect_id of this WritableCircuitTermination.


        :param xconnect_id: The xconnect_id of this WritableCircuitTermination.  # noqa: E501
        :type: str
        """
        if xconnect_id is not None and len(xconnect_id) > 50:
            raise ValueError("Invalid value for `xconnect_id`, length must be less than or equal to `50`")  # noqa: E501

        self._xconnect_id = xconnect_id

    @property
    def pp_info(self):
        """Gets the pp_info of this WritableCircuitTermination.  # noqa: E501


        :return: The pp_info of this WritableCircuitTermination.  # noqa: E501
        :rtype: str
        """
        return self._pp_info

    @pp_info.setter
    def pp_info(self, pp_info):
        """Sets the pp_info of this WritableCircuitTermination.


        :param pp_info: The pp_info of this WritableCircuitTermination.  # noqa: E501
        :type: str
        """
        if pp_info is not None and len(pp_info) > 100:
            raise ValueError("Invalid value for `pp_info`, length must be less than or equal to `100`")  # noqa: E501

        self._pp_info = pp_info

    @property
    def description(self):
        """Gets the description of this WritableCircuitTermination.  # noqa: E501


        :return: The description of this WritableCircuitTermination.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WritableCircuitTermination.


        :param description: The description of this WritableCircuitTermination.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def connected_endpoint_type(self):
        """Gets the connected_endpoint_type of this WritableCircuitTermination.  # noqa: E501


        :return: The connected_endpoint_type of this WritableCircuitTermination.  # noqa: E501
        :rtype: str
        """
        return self._connected_endpoint_type

    @connected_endpoint_type.setter
    def connected_endpoint_type(self, connected_endpoint_type):
        """Sets the connected_endpoint_type of this WritableCircuitTermination.


        :param connected_endpoint_type: The connected_endpoint_type of this WritableCircuitTermination.  # noqa: E501
        :type: str
        """

        self._connected_endpoint_type = connected_endpoint_type

    @property
    def connected_endpoint(self):
        """Gets the connected_endpoint of this WritableCircuitTermination.  # noqa: E501

                 Return the appropriate serializer for the type of connected object.           # noqa: E501

        :return: The connected_endpoint of this WritableCircuitTermination.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._connected_endpoint

    @connected_endpoint.setter
    def connected_endpoint(self, connected_endpoint):
        """Sets the connected_endpoint of this WritableCircuitTermination.

                 Return the appropriate serializer for the type of connected object.           # noqa: E501

        :param connected_endpoint: The connected_endpoint of this WritableCircuitTermination.  # noqa: E501
        :type: dict(str, str)
        """

        self._connected_endpoint = connected_endpoint

    @property
    def connection_status(self):
        """Gets the connection_status of this WritableCircuitTermination.  # noqa: E501


        :return: The connection_status of this WritableCircuitTermination.  # noqa: E501
        :rtype: bool
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """Sets the connection_status of this WritableCircuitTermination.


        :param connection_status: The connection_status of this WritableCircuitTermination.  # noqa: E501
        :type: bool
        """

        self._connection_status = connection_status

    @property
    def cable(self):
        """Gets the cable of this WritableCircuitTermination.  # noqa: E501


        :return: The cable of this WritableCircuitTermination.  # noqa: E501
        :rtype: NestedCable
        """
        return self._cable

    @cable.setter
    def cable(self, cable):
        """Sets the cable of this WritableCircuitTermination.


        :param cable: The cable of this WritableCircuitTermination.  # noqa: E501
        :type: NestedCable
        """

        self._cable = cable

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
        if issubclass(WritableCircuitTermination, dict):
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
        if not isinstance(other, WritableCircuitTermination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
