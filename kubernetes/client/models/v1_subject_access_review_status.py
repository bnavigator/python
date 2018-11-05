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


class V1SubjectAccessReviewStatus(object):
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
        'allowed': 'bool',
        'denied': 'bool',
        'evaluation_error': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'allowed': 'allowed',
        'denied': 'denied',
        'evaluation_error': 'evaluationError',
        'reason': 'reason'
    }

    def __init__(self, allowed=None, denied=None, evaluation_error=None, reason=None):
        """
        V1SubjectAccessReviewStatus - a model defined in Swagger
        """

        self._allowed = None
        self._denied = None
        self._evaluation_error = None
        self._reason = None
        self.discriminator = None

        self.allowed = allowed
        if denied is not None:
          self.denied = denied
        if evaluation_error is not None:
          self.evaluation_error = evaluation_error
        if reason is not None:
          self.reason = reason

    @property
    def allowed(self):
        """
        Gets the allowed of this V1SubjectAccessReviewStatus.
        Allowed is required. True if the action would be allowed, false otherwise.

        :return: The allowed of this V1SubjectAccessReviewStatus.
        :rtype: bool
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """
        Sets the allowed of this V1SubjectAccessReviewStatus.
        Allowed is required. True if the action would be allowed, false otherwise.

        :param allowed: The allowed of this V1SubjectAccessReviewStatus.
        :type: bool
        """
        if allowed is None:
            raise ValueError("Invalid value for `allowed`, must not be `None`")

        self._allowed = allowed

    @property
    def denied(self):
        """
        Gets the denied of this V1SubjectAccessReviewStatus.
        Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true.

        :return: The denied of this V1SubjectAccessReviewStatus.
        :rtype: bool
        """
        return self._denied

    @denied.setter
    def denied(self, denied):
        """
        Sets the denied of this V1SubjectAccessReviewStatus.
        Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true.

        :param denied: The denied of this V1SubjectAccessReviewStatus.
        :type: bool
        """

        self._denied = denied

    @property
    def evaluation_error(self):
        """
        Gets the evaluation_error of this V1SubjectAccessReviewStatus.
        EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request.

        :return: The evaluation_error of this V1SubjectAccessReviewStatus.
        :rtype: str
        """
        return self._evaluation_error

    @evaluation_error.setter
    def evaluation_error(self, evaluation_error):
        """
        Sets the evaluation_error of this V1SubjectAccessReviewStatus.
        EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request.

        :param evaluation_error: The evaluation_error of this V1SubjectAccessReviewStatus.
        :type: str
        """

        self._evaluation_error = evaluation_error

    @property
    def reason(self):
        """
        Gets the reason of this V1SubjectAccessReviewStatus.
        Reason is optional.  It indicates why a request was allowed or denied.

        :return: The reason of this V1SubjectAccessReviewStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1SubjectAccessReviewStatus.
        Reason is optional.  It indicates why a request was allowed or denied.

        :param reason: The reason of this V1SubjectAccessReviewStatus.
        :type: str
        """

        self._reason = reason

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
        if not isinstance(other, V1SubjectAccessReviewStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
