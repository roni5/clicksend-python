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


class DeliveryReceiptRule(object):
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
        'rule_name': 'str',
        'match_type': 'float',
        'action': 'str',
        'action_address': 'str',
        'enabled': 'float'
    }

    attribute_map = {
        'rule_name': 'rule_name',
        'match_type': 'match_type',
        'action': 'action',
        'action_address': 'action_address',
        'enabled': 'enabled'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, rule_name=None, match_type=None, action=None, action_address=None, enabled=None, _configuration=None):  # noqa: E501
        """DeliveryReceiptRule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rule_name = None
        self._match_type = None
        self._action = None
        self._action_address = None
        self._enabled = None
        self.discriminator = 'classType'

        self.rule_name = rule_name
        self.match_type = match_type
        self.action = action
        self.action_address = action_address
        self.enabled = enabled

    @property
    def rule_name(self):
        """Gets the rule_name of this DeliveryReceiptRule.  # noqa: E501

        Rule Name.  # noqa: E501

        :return: The rule_name of this DeliveryReceiptRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this DeliveryReceiptRule.

        Rule Name.  # noqa: E501

        :param rule_name: The rule_name of this DeliveryReceiptRule.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and rule_name is None:
            raise ValueError("Invalid value for `rule_name`, must not be `None`")  # noqa: E501

        self._rule_name = rule_name

    @property
    def match_type(self):
        """Gets the match_type of this DeliveryReceiptRule.  # noqa: E501

        Match Type. 0=All reports.  # noqa: E501

        :return: The match_type of this DeliveryReceiptRule.  # noqa: E501
        :rtype: float
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this DeliveryReceiptRule.

        Match Type. 0=All reports.  # noqa: E501

        :param match_type: The match_type of this DeliveryReceiptRule.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and match_type is None:
            raise ValueError("Invalid value for `match_type`, must not be `None`")  # noqa: E501

        self._match_type = match_type

    @property
    def action(self):
        """Gets the action of this DeliveryReceiptRule.  # noqa: E501

        Action to be taken (AUTO_REPLY, EMAIL_USER, EMAIL_FIXED, URL, SMS, POLL, GROUP_SMS, MOVE_CONTACT, CREATE_CONTACT, CREATE_CONTACT_PLUS_EMAIL, CREATE_CONTACT_PLUS_NAME_EMAIL CREATE_CONTACT_PLUS_NAME, SMPP, NONE).  # noqa: E501

        :return: The action of this DeliveryReceiptRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this DeliveryReceiptRule.

        Action to be taken (AUTO_REPLY, EMAIL_USER, EMAIL_FIXED, URL, SMS, POLL, GROUP_SMS, MOVE_CONTACT, CREATE_CONTACT, CREATE_CONTACT_PLUS_EMAIL, CREATE_CONTACT_PLUS_NAME_EMAIL CREATE_CONTACT_PLUS_NAME, SMPP, NONE).  # noqa: E501

        :param action: The action of this DeliveryReceiptRule.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def action_address(self):
        """Gets the action_address of this DeliveryReceiptRule.  # noqa: E501

        Action address.  # noqa: E501

        :return: The action_address of this DeliveryReceiptRule.  # noqa: E501
        :rtype: str
        """
        return self._action_address

    @action_address.setter
    def action_address(self, action_address):
        """Sets the action_address of this DeliveryReceiptRule.

        Action address.  # noqa: E501

        :param action_address: The action_address of this DeliveryReceiptRule.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and action_address is None:
            raise ValueError("Invalid value for `action_address`, must not be `None`")  # noqa: E501

        self._action_address = action_address

    @property
    def enabled(self):
        """Gets the enabled of this DeliveryReceiptRule.  # noqa: E501

        Enabled: Disabled=0 or Enabled=1.  # noqa: E501

        :return: The enabled of this DeliveryReceiptRule.  # noqa: E501
        :rtype: float
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DeliveryReceiptRule.

        Enabled: Disabled=0 or Enabled=1.  # noqa: E501

        :param enabled: The enabled of this DeliveryReceiptRule.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

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
        if issubclass(DeliveryReceiptRule, dict):
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
        if not isinstance(other, DeliveryReceiptRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeliveryReceiptRule):
            return True

        return self.to_dict() != other.to_dict()
