# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EmailSMSAddress(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      clicksend_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    clicksend_types = {
        'email_address': 'str',
        '_from': 'str',
        'subaccount_id': 'str'
    }

    attribute_map = {
        'email_address': 'email_address',
        '_from': 'from',
        'subaccount_id': 'subaccount_id'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, email_address=None, _from=None, subaccount_id=None):  # noqa: E501
        """EmailSMSAddress - a model defined in Swagger"""  # noqa: E501

        self._email_address = None
        self.__from = None
        self._subaccount_id = None
        self.discriminator = 'classType'

        self.email_address = email_address
        self._from = _from
        if subaccount_id is not None:
            self.subaccount_id = subaccount_id

    @property
    def email_address(self):
        """Gets the email_address of this EmailSMSAddress.  # noqa: E501

        Your email address  # noqa: E501

        :return: The email_address of this EmailSMSAddress.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this EmailSMSAddress.

        Your email address  # noqa: E501

        :param email_address: The email_address of this EmailSMSAddress.  # noqa: E501
        :type: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def _from(self):
        """Gets the _from of this EmailSMSAddress.  # noqa: E501

        Your sender id  # noqa: E501

        :return: The _from of this EmailSMSAddress.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this EmailSMSAddress.

        Your sender id  # noqa: E501

        :param _from: The _from of this EmailSMSAddress.  # noqa: E501
        :type: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def subaccount_id(self):
        """Gets the subaccount_id of this EmailSMSAddress.  # noqa: E501

        Your subaccount id  # noqa: E501

        :return: The subaccount_id of this EmailSMSAddress.  # noqa: E501
        :rtype: str
        """
        return self._subaccount_id

    @subaccount_id.setter
    def subaccount_id(self, subaccount_id):
        """Sets the subaccount_id of this EmailSMSAddress.

        Your subaccount id  # noqa: E501

        :param subaccount_id: The subaccount_id of this EmailSMSAddress.  # noqa: E501
        :type: str
        """

        self._subaccount_id = subaccount_id

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.clicksend_types):
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
        if issubclass(EmailSMSAddress, dict):
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
        if not isinstance(other, EmailSMSAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other