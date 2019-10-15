# coding: utf-8

"""
    ClickSend v3 API

     This is an official SDK for [ClickSend](https://clicksend.com)  Below you will find a current list of the available methods for clicksend.  *NOTE: You will need to create a free account to use the API. You can register [here](https://dashboard.clicksend.com/#/signup/step1/)..*   # noqa: E501

    OpenAPI spec version: 3.1
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


from __future__ import absolute_import

import unittest

import clicksend_client
from clicksend_client.api.sms_api import SMSApi  # noqa: E501
from clicksend_client.rest import ApiException


class TestSMSApi(unittest.TestCase):
    """SMSApi unit test stubs"""

    def setUp(self):
        self.api = clicksend_client.api.sms_api.SMSApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sms_cancel_all_put(self):
        """Test case for sms_cancel_all_put

        Update all scheduled message as cancelled  # noqa: E501
        """
        pass

    def test_sms_cancel_by_message_id_put(self):
        """Test case for sms_cancel_by_message_id_put

        Update scheduled message as cancelled  # noqa: E501
        """
        pass

    def test_sms_history_export_get(self):
        """Test case for sms_history_export_get

        Export all sms history  # noqa: E501
        """
        pass

    def test_sms_history_get(self):
        """Test case for sms_history_get

        Get all sms history  # noqa: E501
        """
        pass

    def test_sms_inbound_get(self):
        """Test case for sms_inbound_get

        Get all inbound sms  # noqa: E501
        """
        pass

    def test_sms_inbound_post(self):
        """Test case for sms_inbound_post

        Create inbound sms  # noqa: E501
        """
        pass

    def test_sms_inbound_read_by_message_id_put(self):
        """Test case for sms_inbound_read_by_message_id_put

        Mark inbound SMS as read  # noqa: E501
        """
        pass

    def test_sms_inbound_read_put(self):
        """Test case for sms_inbound_read_put

        Mark inbound SMS as read  # noqa: E501
        """
        pass

    def test_sms_price_post(self):
        """Test case for sms_price_post

        Calculate sms price  # noqa: E501
        """
        pass

    def test_sms_receipt_read_by_message_id_put(self):
        """Test case for sms_receipt_read_by_message_id_put

        Mark specific delivery receipt as read  # noqa: E501
        """
        pass

    def test_sms_receipts_by_message_id_get(self):
        """Test case for sms_receipts_by_message_id_get

        Get a Specific Delivery Receipt  # noqa: E501
        """
        pass

    def test_sms_receipts_get(self):
        """Test case for sms_receipts_get

        Get all delivery receipts  # noqa: E501
        """
        pass

    def test_sms_receipts_post(self):
        """Test case for sms_receipts_post

        Add a delivery receipt  # noqa: E501
        """
        pass

    def test_sms_receipts_read_put(self):
        """Test case for sms_receipts_read_put

        Mark delivery receipts as read  # noqa: E501
        """
        pass

    def test_sms_send_post(self):
        """Test case for sms_send_post

        Send sms message(s)  # noqa: E501
        """
        pass

    def test_sms_templates_by_template_id_delete(self):
        """Test case for sms_templates_by_template_id_delete

        Delete sms template  # noqa: E501
        """
        pass

    def test_sms_templates_by_template_id_put(self):
        """Test case for sms_templates_by_template_id_put

        Update sms template  # noqa: E501
        """
        pass

    def test_sms_templates_get(self):
        """Test case for sms_templates_get

        Get lists of all sms templates  # noqa: E501
        """
        pass

    def test_sms_templates_post(self):
        """Test case for sms_templates_post

        Create sms template  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
