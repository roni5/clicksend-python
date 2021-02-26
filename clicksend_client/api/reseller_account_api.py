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


class ResellerAccountApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def reseller_accounts_by_client_user_id_get(self, client_user_id, **kwargs):  # noqa: E501
        """Get Reseller clients Account  # noqa: E501

        Get Reseller clients Account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reseller_accounts_by_client_user_id_get(client_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_user_id: User ID of client (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reseller_accounts_by_client_user_id_get_with_http_info(client_user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.reseller_accounts_by_client_user_id_get_with_http_info(client_user_id, **kwargs)  # noqa: E501
            return data

    def reseller_accounts_by_client_user_id_get_with_http_info(self, client_user_id, **kwargs):  # noqa: E501
        """Get Reseller clients Account  # noqa: E501

        Get Reseller clients Account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reseller_accounts_by_client_user_id_get_with_http_info(client_user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_user_id: User ID of client (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reseller_accounts_by_client_user_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_user_id' is set
        if self.api_client.client_side_validation and ('client_user_id' not in params or
                                                       params['client_user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `client_user_id` when calling `reseller_accounts_by_client_user_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_user_id' in params:
            path_params['client_user_id'] = params['client_user_id']  # noqa: E501

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
            '/reseller/accounts/{client_user_id}', 'GET',
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

    def reseller_accounts_by_client_user_id_put(self, client_user_id, reseller_account, **kwargs):  # noqa: E501
        """Update Reseller clients Account  # noqa: E501

        Update Reseller clients Account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reseller_accounts_by_client_user_id_put(client_user_id, reseller_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_user_id: User ID of client (required)
        :param ResellerAccount reseller_account: ResellerAccount model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reseller_accounts_by_client_user_id_put_with_http_info(client_user_id, reseller_account, **kwargs)  # noqa: E501
        else:
            (data) = self.reseller_accounts_by_client_user_id_put_with_http_info(client_user_id, reseller_account, **kwargs)  # noqa: E501
            return data

    def reseller_accounts_by_client_user_id_put_with_http_info(self, client_user_id, reseller_account, **kwargs):  # noqa: E501
        """Update Reseller clients Account  # noqa: E501

        Update Reseller clients Account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reseller_accounts_by_client_user_id_put_with_http_info(client_user_id, reseller_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_user_id: User ID of client (required)
        :param ResellerAccount reseller_account: ResellerAccount model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_user_id', 'reseller_account']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reseller_accounts_by_client_user_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_user_id' is set
        if self.api_client.client_side_validation and ('client_user_id' not in params or
                                                       params['client_user_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `client_user_id` when calling `reseller_accounts_by_client_user_id_put`")  # noqa: E501
        # verify the required parameter 'reseller_account' is set
        if self.api_client.client_side_validation and ('reseller_account' not in params or
                                                       params['reseller_account'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `reseller_account` when calling `reseller_accounts_by_client_user_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'client_user_id' in params:
            path_params['client_user_id'] = params['client_user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reseller_account' in params:
            body_params = params['reseller_account']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/reseller/accounts/{client_user_id}', 'PUT',
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

    def reseller_accounts_get(self, **kwargs):  # noqa: E501
        """Get list of reseller accounts  # noqa: E501

        Get list of reseller accounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reseller_accounts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reseller_accounts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.reseller_accounts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def reseller_accounts_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of reseller accounts  # noqa: E501

        Get list of reseller accounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reseller_accounts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reseller_accounts_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `reseller_accounts_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `reseller_accounts_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/reseller/accounts', 'GET',
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

    def reseller_accounts_post(self, reseller_account, **kwargs):  # noqa: E501
        """Create reseller account  # noqa: E501

        Create reseller account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reseller_accounts_post(reseller_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResellerAccount reseller_account: ResellerAccount model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reseller_accounts_post_with_http_info(reseller_account, **kwargs)  # noqa: E501
        else:
            (data) = self.reseller_accounts_post_with_http_info(reseller_account, **kwargs)  # noqa: E501
            return data

    def reseller_accounts_post_with_http_info(self, reseller_account, **kwargs):  # noqa: E501
        """Create reseller account  # noqa: E501

        Create reseller account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reseller_accounts_post_with_http_info(reseller_account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ResellerAccount reseller_account: ResellerAccount model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reseller_account']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reseller_accounts_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reseller_account' is set
        if self.api_client.client_side_validation and ('reseller_account' not in params or
                                                       params['reseller_account'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `reseller_account` when calling `reseller_accounts_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reseller_account' in params:
            body_params = params['reseller_account']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/reseller/accounts', 'POST',
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
