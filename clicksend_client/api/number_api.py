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


class NumberApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def numbers_buy_by_dedicated_number_post(self, dedicated_number, **kwargs):  # noqa: E501
        """Buy dedicated number  # noqa: E501

        Buy dedicated number  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.numbers_buy_by_dedicated_number_post(dedicated_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dedicated_number: Phone number to purchase (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.numbers_buy_by_dedicated_number_post_with_http_info(dedicated_number, **kwargs)  # noqa: E501
        else:
            (data) = self.numbers_buy_by_dedicated_number_post_with_http_info(dedicated_number, **kwargs)  # noqa: E501
            return data

    def numbers_buy_by_dedicated_number_post_with_http_info(self, dedicated_number, **kwargs):  # noqa: E501
        """Buy dedicated number  # noqa: E501

        Buy dedicated number  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.numbers_buy_by_dedicated_number_post_with_http_info(dedicated_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dedicated_number: Phone number to purchase (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dedicated_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method numbers_buy_by_dedicated_number_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dedicated_number' is set
        if self.api_client.client_side_validation and ('dedicated_number' not in params or
                                                       params['dedicated_number'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `dedicated_number` when calling `numbers_buy_by_dedicated_number_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dedicated_number' in params:
            path_params['dedicated_number'] = params['dedicated_number']  # noqa: E501

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
            '/numbers/buy/{dedicated_number}', 'POST',
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

    def numbers_get(self, **kwargs):  # noqa: E501
        """Get all availible dedicated numbers  # noqa: E501

        Get all availible dedicated numbers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.numbers_get(async_req=True)
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
            return self.numbers_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.numbers_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def numbers_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all availible dedicated numbers  # noqa: E501

        Get all availible dedicated numbers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.numbers_get_with_http_info(async_req=True)
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
                    " to method numbers_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `numbers_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `numbers_get`, must be a value greater than or equal to `1`")  # noqa: E501
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
            '/numbers', 'GET',
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

    def numbers_search_by_country_get(self, country, **kwargs):  # noqa: E501
        """Get all dedicated numbers by country  # noqa: E501

        Get all dedicated numbers by country  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.numbers_search_by_country_get(country, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: Country code to search (required)
        :param str search: Your search pattern or query.
        :param int search_type: Your strategy for searching, 0 = starts with, 1 = anywhere, 2 = ends with.
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.numbers_search_by_country_get_with_http_info(country, **kwargs)  # noqa: E501
        else:
            (data) = self.numbers_search_by_country_get_with_http_info(country, **kwargs)  # noqa: E501
            return data

    def numbers_search_by_country_get_with_http_info(self, country, **kwargs):  # noqa: E501
        """Get all dedicated numbers by country  # noqa: E501

        Get all dedicated numbers by country  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.numbers_search_by_country_get_with_http_info(country, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: Country code to search (required)
        :param str search: Your search pattern or query.
        :param int search_type: Your strategy for searching, 0 = starts with, 1 = anywhere, 2 = ends with.
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country', 'search', 'search_type', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method numbers_search_by_country_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country' is set
        if self.api_client.client_side_validation and ('country' not in params or
                                                       params['country'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `country` when calling `numbers_search_by_country_get`")  # noqa: E501

        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `numbers_search_by_country_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `numbers_search_by_country_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'country' in params:
            path_params['country'] = params['country']  # noqa: E501

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'search_type' in params:
            query_params.append(('search_type', params['search_type']))  # noqa: E501
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
            '/numbers/search/{country}', 'GET',
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
