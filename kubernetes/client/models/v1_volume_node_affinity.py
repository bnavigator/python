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


class V1VolumeNodeAffinity(object):
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
        'required': 'V1NodeSelector'
    }

    attribute_map = {
        'required': 'required'
    }

    def __init__(self, required=None):
        """
        V1VolumeNodeAffinity - a model defined in Swagger
        """

        self._required = None
        self.discriminator = None

        if required is not None:
          self.required = required

    @property
    def required(self):
        """
        Gets the required of this V1VolumeNodeAffinity.
        Required specifies hard node constraints that must be met.

        :return: The required of this V1VolumeNodeAffinity.
        :rtype: V1NodeSelector
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this V1VolumeNodeAffinity.
        Required specifies hard node constraints that must be met.

        :param required: The required of this V1VolumeNodeAffinity.
        :type: V1NodeSelector
        """

        self._required = required

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
        if not isinstance(other, V1VolumeNodeAffinity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
