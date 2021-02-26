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


class MasterEmailTemplatesApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def master_email_template_categories_get(self, **kwargs):  # noqa: E501
        """Get all master email template categories  # noqa: E501

        Get all master email template categories  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.master_email_template_categories_get(async_req=True)
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
            return self.master_email_template_categories_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.master_email_template_categories_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def master_email_template_categories_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all master email template categories  # noqa: E501

        Get all master email template categories  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.master_email_template_categories_get_with_http_info(async_req=True)
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
                    " to method master_email_template_categories_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `master_email_template_categories_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `master_email_template_categories_get`, must be a value greater than or equal to `1`")  # noqa: E501
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
            '/email/master-templates-categories', 'GET',
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

    def master_email_template_category_get(self, category_id, **kwargs):  # noqa: E501
        """Get specific master email template category  # noqa: E501

        Get specific master email template category  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.master_email_template_category_get(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int category_id: Email category id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.master_email_template_category_get_with_http_info(category_id, **kwargs)  # noqa: E501
        else:
            (data) = self.master_email_template_category_get_with_http_info(category_id, **kwargs)  # noqa: E501
            return data

    def master_email_template_category_get_with_http_info(self, category_id, **kwargs):  # noqa: E501
        """Get specific master email template category  # noqa: E501

        Get specific master email template category  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.master_email_template_category_get_with_http_info(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int category_id: Email category id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method master_email_template_category_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if self.api_client.client_side_validation and ('category_id' not in params or
                                                       params['category_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `category_id` when calling `master_email_template_category_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'category_id' in params:
            path_params['category_id'] = params['category_id']  # noqa: E501

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
            '/email/master-templates-categories/{category_id}', 'GET',
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

    def master_email_template_get(self, template_id, **kwargs):  # noqa: E501
        """Get specific master email template  # noqa: E501

        Get specific master email template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.master_email_template_get(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int template_id: Email template id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.master_email_template_get_with_http_info(template_id, **kwargs)  # noqa: E501
        else:
            (data) = self.master_email_template_get_with_http_info(template_id, **kwargs)  # noqa: E501
            return data

    def master_email_template_get_with_http_info(self, template_id, **kwargs):  # noqa: E501
        """Get specific master email template  # noqa: E501

        Get specific master email template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.master_email_template_get_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int template_id: Email template id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method master_email_template_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'template_id' is set
        if self.api_client.client_side_validation and ('template_id' not in params or
                                                       params['template_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `template_id` when calling `master_email_template_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in params:
            path_params['template_id'] = params['template_id']  # noqa: E501

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
            '/email/master-templates/{template_id}', 'GET',
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

    def master_email_templates_get(self, **kwargs):  # noqa: E501
        """Get all master email templates  # noqa: E501

        Get all master email templates  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.master_email_templates_get(async_req=True)
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
            return self.master_email_templates_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.master_email_templates_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def master_email_templates_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all master email templates  # noqa: E501

        Get all master email templates  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.master_email_templates_get_with_http_info(async_req=True)
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
                    " to method master_email_templates_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `master_email_templates_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `master_email_templates_get`, must be a value greater than or equal to `1`")  # noqa: E501
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
            '/email/master-templates', 'GET',
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

    def master_email_templates_in_category_get(self, category_id, **kwargs):  # noqa: E501
        """Get all master email templates in a category  # noqa: E501

        Get all master email templates in a category  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.master_email_templates_in_category_get(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int category_id: Email category id (required)
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.master_email_templates_in_category_get_with_http_info(category_id, **kwargs)  # noqa: E501
        else:
            (data) = self.master_email_templates_in_category_get_with_http_info(category_id, **kwargs)  # noqa: E501
            return data

    def master_email_templates_in_category_get_with_http_info(self, category_id, **kwargs):  # noqa: E501
        """Get all master email templates in a category  # noqa: E501

        Get all master email templates in a category  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.master_email_templates_in_category_get_with_http_info(category_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int category_id: Email category id (required)
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method master_email_templates_in_category_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if self.api_client.client_side_validation and ('category_id' not in params or
                                                       params['category_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `category_id` when calling `master_email_templates_in_category_get`")  # noqa: E501

        if self.api_client.client_side_validation and ('page' in params and params['page'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `master_email_templates_in_category_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `master_email_templates_in_category_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'category_id' in params:
            path_params['category_id'] = params['category_id']  # noqa: E501

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
            '/email/master-templates-categories/{category_id}/master-templates', 'GET',
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
