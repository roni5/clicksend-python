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


class Attachment(object):
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
        'content': 'str',
        'type': 'str',
        'filename': 'str',
        'disposition': 'str',
        'content_id': 'str'
    }

    attribute_map = {
        'content': 'content',
        'type': 'type',
        'filename': 'filename',
        'disposition': 'disposition',
        'content_id': 'content_id'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, content=None, type=None, filename=None, disposition=None, content_id=None, _configuration=None):  # noqa: E501
        """Attachment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._content = None
        self._type = None
        self._filename = None
        self._disposition = None
        self._content_id = None
        self.discriminator = 'classType'

        self.content = content
        self.type = type
        self.filename = filename
        self.disposition = disposition
        self.content_id = content_id

    @property
    def content(self):
        """Gets the content of this Attachment.  # noqa: E501

        The base64-encoded contents of the file.  # noqa: E501

        :return: The content of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Attachment.

        The base64-encoded contents of the file.  # noqa: E501

        :param content: The content of this Attachment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def type(self):
        """Gets the type of this Attachment.  # noqa: E501

        The type of file being attached.  # noqa: E501

        :return: The type of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Attachment.

        The type of file being attached.  # noqa: E501

        :param type: The type of this Attachment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def filename(self):
        """Gets the filename of this Attachment.  # noqa: E501

        The name of the file being attached.  # noqa: E501

        :return: The filename of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Attachment.

        The name of the file being attached.  # noqa: E501

        :param filename: The filename of this Attachment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def disposition(self):
        """Gets the disposition of this Attachment.  # noqa: E501

        Inline for content that can be displayed within the email, or attachment for any other files.  # noqa: E501

        :return: The disposition of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._disposition

    @disposition.setter
    def disposition(self, disposition):
        """Sets the disposition of this Attachment.

        Inline for content that can be displayed within the email, or attachment for any other files.  # noqa: E501

        :param disposition: The disposition of this Attachment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and disposition is None:
            raise ValueError("Invalid value for `disposition`, must not be `None`")  # noqa: E501

        self._disposition = disposition

    @property
    def content_id(self):
        """Gets the content_id of this Attachment.  # noqa: E501

        An ID for the content.  # noqa: E501

        :return: The content_id of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        """Sets the content_id of this Attachment.

        An ID for the content.  # noqa: E501

        :param content_id: The content_id of this Attachment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and content_id is None:
            raise ValueError("Invalid value for `content_id`, must not be `None`")  # noqa: E501

        self._content_id = content_id

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
        if issubclass(Attachment, dict):
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
        if not isinstance(other, Attachment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Attachment):
            return True

        return self.to_dict() != other.to_dict()
