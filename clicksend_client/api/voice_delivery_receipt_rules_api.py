# coding: utf-8

"""
    ClickSend v3 API

     This is an official SDK for [ClickSend](https://clicksend.com)  Below you will find a current list of the available methods for clicksend.  *NOTE: You will need to create a free account to use the API. You can register [here](https://dashboard.clicksend.com/#/signup/step1/)..*   # noqa: E501

    OpenAPI spec version: 3.1
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from clicksend_client.api_client import ApiClient


class VoiceDeliveryReceiptRulesApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def voice_delivery_receipt_automation_delete(self, receipt_rule_id, **kwargs):  # noqa: E501
        """Delete voice delivery receipt automation  # noqa: E501

        Delete voice delivery receipt automation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_delivery_receipt_automation_delete(receipt_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int receipt_rule_id: Receipt rule id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_delivery_receipt_automation_delete_with_http_info(receipt_rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.voice_delivery_receipt_automation_delete_with_http_info(receipt_rule_id, **kwargs)  # noqa: E501
            return data

    def voice_delivery_receipt_automation_delete_with_http_info(self, receipt_rule_id, **kwargs):  # noqa: E501
        """Delete voice delivery receipt automation  # noqa: E501

        Delete voice delivery receipt automation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_delivery_receipt_automation_delete_with_http_info(receipt_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int receipt_rule_id: Receipt rule id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['receipt_rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_delivery_receipt_automation_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'receipt_rule_id' is set
        if self.api_client.client_side_validation and ('receipt_rule_id' not in params or
                                                       params['receipt_rule_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `receipt_rule_id` when calling `voice_delivery_receipt_automation_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'receipt_rule_id' in params:
            path_params['receipt_rule_id'] = params['receipt_rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/automations/voice/receipts/{receipt_rule_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def voice_delivery_receipt_automation_get(self, receipt_rule_id, **kwargs):  # noqa: E501
        """Get specific voice delivery receipt automation  # noqa: E501

        Get specific voice delivery receipt automation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_delivery_receipt_automation_get(receipt_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int receipt_rule_id: Receipt rule id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_delivery_receipt_automation_get_with_http_info(receipt_rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.voice_delivery_receipt_automation_get_with_http_info(receipt_rule_id, **kwargs)  # noqa: E501
            return data

    def voice_delivery_receipt_automation_get_with_http_info(self, receipt_rule_id, **kwargs):  # noqa: E501
        """Get specific voice delivery receipt automation  # noqa: E501

        Get specific voice delivery receipt automation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_delivery_receipt_automation_get_with_http_info(receipt_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int receipt_rule_id: Receipt rule id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['receipt_rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_delivery_receipt_automation_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'receipt_rule_id' is set
        if self.api_client.client_side_validation and ('receipt_rule_id' not in params or
                                                       params['receipt_rule_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `receipt_rule_id` when calling `voice_delivery_receipt_automation_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'receipt_rule_id' in params:
            path_params['receipt_rule_id'] = params['receipt_rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/automations/voice/receipts/{receipt_rule_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def voice_delivery_receipt_automation_post(self, delivery_receipt_rule, **kwargs):  # noqa: E501
        """Create voice delivery receipt automations  # noqa: E501

        Create voice delivery receipt automations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_delivery_receipt_automation_post(delivery_receipt_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryReceiptRule delivery_receipt_rule: voice delivery receipt rule model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_delivery_receipt_automation_post_with_http_info(delivery_receipt_rule, **kwargs)  # noqa: E501
        else:
            (data) = self.voice_delivery_receipt_automation_post_with_http_info(delivery_receipt_rule, **kwargs)  # noqa: E501
            return data

    def voice_delivery_receipt_automation_post_with_http_info(self, delivery_receipt_rule, **kwargs):  # noqa: E501
        """Create voice delivery receipt automations  # noqa: E501

        Create voice delivery receipt automations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_delivery_receipt_automation_post_with_http_info(delivery_receipt_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeliveryReceiptRule delivery_receipt_rule: voice delivery receipt rule model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delivery_receipt_rule']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_delivery_receipt_automation_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delivery_receipt_rule' is set
        if self.api_client.client_side_validation and ('delivery_receipt_rule' not in params or
                                                       params['delivery_receipt_rule'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `delivery_receipt_rule` when calling `voice_delivery_receipt_automation_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'delivery_receipt_rule' in params:
            body_params = params['delivery_receipt_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/automations/voice/receipts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def voice_delivery_receipt_automation_put(self, receipt_rule_id, delivery_receipt_rule, **kwargs):  # noqa: E501
        """Update voice delivery receipt automation  # noqa: E501

        Update voice delivery receipt automation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_delivery_receipt_automation_put(receipt_rule_id, delivery_receipt_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int receipt_rule_id: Receipt rule id (required)
        :param DeliveryReceiptRule delivery_receipt_rule: Delivery receipt rule model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_delivery_receipt_automation_put_with_http_info(receipt_rule_id, delivery_receipt_rule, **kwargs)  # noqa: E501
        else:
            (data) = self.voice_delivery_receipt_automation_put_with_http_info(receipt_rule_id, delivery_receipt_rule, **kwargs)  # noqa: E501
            return data

    def voice_delivery_receipt_automation_put_with_http_info(self, receipt_rule_id, delivery_receipt_rule, **kwargs):  # noqa: E501
        """Update voice delivery receipt automation  # noqa: E501

        Update voice delivery receipt automation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_delivery_receipt_automation_put_with_http_info(receipt_rule_id, delivery_receipt_rule, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int receipt_rule_id: Receipt rule id (required)
        :param DeliveryReceiptRule delivery_receipt_rule: Delivery receipt rule model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['receipt_rule_id', 'delivery_receipt_rule']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_delivery_receipt_automation_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'receipt_rule_id' is set
        if self.api_client.client_side_validation and ('receipt_rule_id' not in params or
                                                       params['receipt_rule_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `receipt_rule_id` when calling `voice_delivery_receipt_automation_put`")  # noqa: E501
        # verify the required parameter 'delivery_receipt_rule' is set
        if self.api_client.client_side_validation and ('delivery_receipt_rule' not in params or
                                                       params['delivery_receipt_rule'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `delivery_receipt_rule` when calling `voice_delivery_receipt_automation_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'receipt_rule_id' in params:
            path_params['receipt_rule_id'] = params['receipt_rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'delivery_receipt_rule' in params:
            body_params = params['delivery_receipt_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/automations/voice/receipts/{receipt_rule_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def voice_delivery_receipt_automations_get(self, **kwargs):  # noqa: E501
        """Get all voice delivery receipt automations  # noqa: E501

        Get all voice delivery receipt automations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_delivery_receipt_automations_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: Your keyword or query.
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_delivery_receipt_automations_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.voice_delivery_receipt_automations_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def voice_delivery_receipt_automations_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all voice delivery receipt automations  # noqa: E501

        Get all voice delivery receipt automations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_delivery_receipt_automations_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: Your keyword or query.
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_delivery_receipt_automations_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `voice_delivery_receipt_automations_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `voice_delivery_receipt_automations_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/automations/voice/receipts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
