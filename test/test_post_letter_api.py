# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from clicksend.api.post_letter_api import PostLetterApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPostLetterApi(unittest.TestCase):
    """PostLetterApi unit test stubs"""

    def setUp(self):
        self.api = clicksend.api.post_letter_api.PostLetterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_letters_export_get(self):
        """Test case for post_letters_export_get

        export post letter history  # noqa: E501
        """
        pass

    def test_post_letters_history_get(self):
        """Test case for post_letters_history_get

        Get all post letter history  # noqa: E501
        """
        pass

    def test_post_letters_price_post(self):
        """Test case for post_letters_price_post

        Calculate post letter price  # noqa: E501
        """
        pass

    def test_post_letters_send_post(self):
        """Test case for post_letters_send_post

        Send post letter  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
