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


class FaxMessage(object):
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
        'source': 'str',
        'to': 'str',
        'list_id': 'int',
        '_from': 'str',
        'schedule': 'int',
        'custom_string': 'str',
        'country': 'str',
        'from_email': 'str'
    }

    attribute_map = {
        'source': 'source',
        'to': 'to',
        'list_id': 'list_id',
        '_from': 'from',
        'schedule': 'schedule',
        'custom_string': 'custom_string',
        'country': 'country',
        'from_email': 'from_email'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, source='sdk', to=None, list_id=None, _from=None, schedule=None, custom_string=None, country=None, from_email=None, _configuration=None):  # noqa: E501
        """FaxMessage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._source = None
        self._to = None
        self._list_id = None
        self.__from = None
        self._schedule = None
        self._custom_string = None
        self._country = None
        self._from_email = None
        self.discriminator = 'classType'

        if source is not None:
            self.source = source
        self.to = to
        if list_id is not None:
            self.list_id = list_id
        if _from is not None:
            self._from = _from
        if schedule is not None:
            self.schedule = schedule
        if custom_string is not None:
            self.custom_string = custom_string
        if country is not None:
            self.country = country
        if from_email is not None:
            self.from_email = from_email

    @property
    def source(self):
        """Gets the source of this FaxMessage.  # noqa: E501

        Your method of sending e.g. 'wordpress', 'php', 'c#'.  # noqa: E501

        :return: The source of this FaxMessage.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this FaxMessage.

        Your method of sending e.g. 'wordpress', 'php', 'c#'.  # noqa: E501

        :param source: The source of this FaxMessage.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def to(self):
        """Gets the to of this FaxMessage.  # noqa: E501

        Recipient fax number in E.164 format.  # noqa: E501

        :return: The to of this FaxMessage.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this FaxMessage.

        Recipient fax number in E.164 format.  # noqa: E501

        :param to: The to of this FaxMessage.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def list_id(self):
        """Gets the list_id of this FaxMessage.  # noqa: E501

        Your list ID if sending to a whole list. Can be used instead of 'to'.  # noqa: E501

        :return: The list_id of this FaxMessage.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this FaxMessage.

        Your list ID if sending to a whole list. Can be used instead of 'to'.  # noqa: E501

        :param list_id: The list_id of this FaxMessage.  # noqa: E501
        :type: int
        """

        self._list_id = list_id

    @property
    def _from(self):
        """Gets the _from of this FaxMessage.  # noqa: E501

        Your sender id. Must be a valid fax number.  # noqa: E501

        :return: The _from of this FaxMessage.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this FaxMessage.

        Your sender id. Must be a valid fax number.  # noqa: E501

        :param _from: The _from of this FaxMessage.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def schedule(self):
        """Gets the schedule of this FaxMessage.  # noqa: E501

        Leave blank for immediate delivery. Your schedule time in unix format http://help.clicksend.com/what-is-a-unix-timestamp  # noqa: E501

        :return: The schedule of this FaxMessage.  # noqa: E501
        :rtype: int
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this FaxMessage.

        Leave blank for immediate delivery. Your schedule time in unix format http://help.clicksend.com/what-is-a-unix-timestamp  # noqa: E501

        :param schedule: The schedule of this FaxMessage.  # noqa: E501
        :type: int
        """

        self._schedule = schedule

    @property
    def custom_string(self):
        """Gets the custom_string of this FaxMessage.  # noqa: E501

        Your reference. Will be passed back with all replies and delivery reports.  # noqa: E501

        :return: The custom_string of this FaxMessage.  # noqa: E501
        :rtype: str
        """
        return self._custom_string

    @custom_string.setter
    def custom_string(self, custom_string):
        """Sets the custom_string of this FaxMessage.

        Your reference. Will be passed back with all replies and delivery reports.  # noqa: E501

        :param custom_string: The custom_string of this FaxMessage.  # noqa: E501
        :type: str
        """

        self._custom_string = custom_string

    @property
    def country(self):
        """Gets the country of this FaxMessage.  # noqa: E501

        Recipient country.  # noqa: E501

        :return: The country of this FaxMessage.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this FaxMessage.

        Recipient country.  # noqa: E501

        :param country: The country of this FaxMessage.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def from_email(self):
        """Gets the from_email of this FaxMessage.  # noqa: E501

        An email address where the reply should be emailed to.  # noqa: E501

        :return: The from_email of this FaxMessage.  # noqa: E501
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """Sets the from_email of this FaxMessage.

        An email address where the reply should be emailed to.  # noqa: E501

        :param from_email: The from_email of this FaxMessage.  # noqa: E501
        :type: str
        """

        self._from_email = from_email

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
        if issubclass(FaxMessage, dict):
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
        if not isinstance(other, FaxMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FaxMessage):
            return True

        return self.to_dict() != other.to_dict()
