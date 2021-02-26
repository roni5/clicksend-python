# coding: utf-8

"""
    ClickSend v3 API

     This is an official SDK for [ClickSend](https://clicksend.com)  Below you will find a current list of the available methods for clicksend.  *NOTE: You will need to create a free account to use the API. You can register [here](https://dashboard.clicksend.com/#/signup/step1/)..*   # noqa: E501

    OpenAPI spec version: 3.1
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from clicksend_client.configuration import Configuration


class SmsMessageCollection(object):
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
        'messages': 'list[SmsMessage]'
    }

    attribute_map = {
        'messages': 'messages'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, messages=None, _configuration=None):  # noqa: E501
        """SmsMessageCollection - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._messages = None
        self.discriminator = 'classType'

        self.messages = messages

    @property
    def messages(self):
        """Gets the messages of this SmsMessageCollection.  # noqa: E501

        Array of SmsMessage items  # noqa: E501

        :return: The messages of this SmsMessageCollection.  # noqa: E501
        :rtype: list[SmsMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this SmsMessageCollection.

        Array of SmsMessage items  # noqa: E501

        :param messages: The messages of this SmsMessageCollection.  # noqa: E501
        :type: list[SmsMessage]
        """
        if self._configuration.client_side_validation and messages is None:
            raise ValueError("Invalid value for `messages`, must not be `None`")  # noqa: E501

        self._messages = messages

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
        if issubclass(SmsMessageCollection, dict):
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
        if not isinstance(other, SmsMessageCollection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmsMessageCollection):
            return True

        return self.to_dict() != other.to_dict()
