# coding: utf-8

"""
    CIRA SHG Windex API

    CIRALabs SecureHomeGateway Windex API: between smartphone and router  # noqa: E501

    OpenAPI spec version: 1.0.0-current
    Contact: securehomegateway@cira.ca
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from client.api_client import ApiClient
from client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ManufacturerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_manufacturer(self, manufacturer_body, **kwargs):  # noqa: E501
        """Add a new manufacturer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_manufacturer(manufacturer_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ManufacturerBody manufacturer_body: Manufacturer object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_manufacturer_with_http_info(manufacturer_body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_manufacturer_with_http_info(manufacturer_body, **kwargs)  # noqa: E501
            return data

    def create_manufacturer_with_http_info(self, manufacturer_body, **kwargs):  # noqa: E501
        """Add a new manufacturer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_manufacturer_with_http_info(manufacturer_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ManufacturerBody manufacturer_body: Manufacturer object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['manufacturer_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_manufacturer" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'manufacturer_body' is set
        if ('manufacturer_body' not in local_var_params or
                local_var_params['manufacturer_body'] is None):
            raise ApiValueError("Missing the required parameter `manufacturer_body` when calling `create_manufacturer`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'manufacturer_body' in local_var_params:
            body_params = local_var_params['manufacturer_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/manufacturers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_manufacturer(self, id, **kwargs):  # noqa: E501
        """Get a manufacturer information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manufacturer(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of the device (required)
        :return: Manufacturer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_manufacturer_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_manufacturer_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_manufacturer_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a manufacturer information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_manufacturer_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of the device (required)
        :return: Manufacturer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manufacturer" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `get_manufacturer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/manufacturers/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Manufacturer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_manufacturers(self, **kwargs):  # noqa: E501
        """Get manufacturers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_manufacturers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_manufacturers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_manufacturers_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_manufacturers_with_http_info(self, **kwargs):  # noqa: E501
        """Get manufacturers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_manufacturers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_manufacturers" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/manufacturers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_manufacturer(self, id, manufacturer_body, **kwargs):  # noqa: E501
        """Update an existing manufacturer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_manufacturer(id, manufacturer_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of the device (required)
        :param ManufacturerBody manufacturer_body: Manufacturer object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_manufacturer_with_http_info(id, manufacturer_body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_manufacturer_with_http_info(id, manufacturer_body, **kwargs)  # noqa: E501
            return data

    def update_manufacturer_with_http_info(self, id, manufacturer_body, **kwargs):  # noqa: E501
        """Update an existing manufacturer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_manufacturer_with_http_info(id, manufacturer_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of the device (required)
        :param ManufacturerBody manufacturer_body: Manufacturer object (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'manufacturer_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_manufacturer" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `update_manufacturer`")  # noqa: E501
        # verify the required parameter 'manufacturer_body' is set
        if ('manufacturer_body' not in local_var_params or
                local_var_params['manufacturer_body'] is None):
            raise ApiValueError("Missing the required parameter `manufacturer_body` when calling `update_manufacturer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'manufacturer_body' in local_var_params:
            body_params = local_var_params['manufacturer_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/manufacturers/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)