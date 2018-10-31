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
from ClickSend.Client.Api.upload_api import UploadApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUploadApi(unittest.TestCase):
    """UploadApi unit test stubs"""

    def setUp(self):
        self.api = ClickSend.Client.Api.upload_api.UploadApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_uploads_post(self):
        """Test case for uploads_post

        Upload File  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
