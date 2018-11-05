# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1QuobyteVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'group': 'str',
        'read_only': 'bool',
        'registry': 'str',
        'user': 'str',
        'volume': 'str'
    }

    attribute_map = {
        'group': 'group',
        'read_only': 'readOnly',
        'registry': 'registry',
        'user': 'user',
        'volume': 'volume'
    }

    def __init__(self, group=None, read_only=None, registry=None, user=None, volume=None):
        """
        V1QuobyteVolumeSource - a model defined in Swagger
        """

        self._group = None
        self._read_only = None
        self._registry = None
        self._user = None
        self._volume = None
        self.discriminator = None

        if group is not None:
          self.group = group
        if read_only is not None:
          self.read_only = read_only
        self.registry = registry
        if user is not None:
          self.user = user
        self.volume = volume

    @property
    def group(self):
        """
        Gets the group of this V1QuobyteVolumeSource.
        Group to map volume access to Default is no group

        :return: The group of this V1QuobyteVolumeSource.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this V1QuobyteVolumeSource.
        Group to map volume access to Default is no group

        :param group: The group of this V1QuobyteVolumeSource.
        :type: str
        """

        self._group = group

    @property
    def read_only(self):
        """
        Gets the read_only of this V1QuobyteVolumeSource.
        ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.

        :return: The read_only of this V1QuobyteVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1QuobyteVolumeSource.
        ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.

        :param read_only: The read_only of this V1QuobyteVolumeSource.
        :type: bool
        """

        self._read_only = read_only

    @property
    def registry(self):
        """
        Gets the registry of this V1QuobyteVolumeSource.
        Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes

        :return: The registry of this V1QuobyteVolumeSource.
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """
        Sets the registry of this V1QuobyteVolumeSource.
        Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes

        :param registry: The registry of this V1QuobyteVolumeSource.
        :type: str
        """
        if registry is None:
            raise ValueError("Invalid value for `registry`, must not be `None`")

        self._registry = registry

    @property
    def user(self):
        """
        Gets the user of this V1QuobyteVolumeSource.
        User to map volume access to Defaults to serivceaccount user

        :return: The user of this V1QuobyteVolumeSource.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this V1QuobyteVolumeSource.
        User to map volume access to Defaults to serivceaccount user

        :param user: The user of this V1QuobyteVolumeSource.
        :type: str
        """

        self._user = user

    @property
    def volume(self):
        """
        Gets the volume of this V1QuobyteVolumeSource.
        Volume is a string that references an already created Quobyte volume by name.

        :return: The volume of this V1QuobyteVolumeSource.
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """
        Sets the volume of this V1QuobyteVolumeSource.
        Volume is a string that references an already created Quobyte volume by name.

        :param volume: The volume of this V1QuobyteVolumeSource.
        :type: str
        """
        if volume is None:
            raise ValueError("Invalid value for `volume`, must not be `None`")

        self._volume = volume

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1QuobyteVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
