"""
    SeadataNet API

    A detailed description of the operation.  # noqa: E501

    The version of the OpenAPI document: 5.1.0
    Contact: info@maris.nl
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from sdnclient.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from sdnclient.exceptions import ApiAttributeError


def lazy_import():
    from sdnclient.model.order_query_query_fields import OrderQueryQueryFields
    globals()['OrderQueryQueryFields'] = OrderQueryQueryFields


class MetadataQuery(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('facet_fields',): {
            'MEASURING_AREA_TYPE_L02': "measuring_area_type_l02",
            'PARAMETERS_P02': "parameters_p02",
            'PARAMETERS_P03': "parameters_p03",
            'PARAMETERS_P08': "parameters_p08",
            'AUTHOR_EDMO': "author_edmo",
            'AUTHOR_EDMO_COUNTRY': "author_edmo_country",
            'ORIGINATOR_EDMO': "originator_edmo",
            'CUSTODIUM_EDMO': "custodium_edmo",
            'DISTRIBUTOR_EDMO': "distributor_edmo",
        },
        ('return_fields',): {
            'N_CODE': "n_code",
            'DATANAME': "dataname",
            'CDI_IDENTIFIER': "cdi_identifier",
            'C_ORIGINATOR_EDMO_COUNTRY': "c_originator_edmo_country",
            'START_DATE': "start_date",
            'END_DATE': "end_date",
            'C_INSTRUMENT_L05': "c_instrument_l05",
            'VERSION': "version",
            'DATA_FORMAT_L24': "data_format_l24",
            'BBOX_NORTH': "bbox_north",
            'BBOX_EAST': "bbox_east",
            'BBOX_SOUTH': "bbox_south",
            'BBOX_WEST': "bbox_west",
            'C_MEASURING_AREA_TYPE_L02': "c_measuring_area_type_l02",
        },
        ('pagination_sort',): {
            'N_CODE': "n_code",
            'DATANAME': "dataname",
            'CDI_IDENTIFIER': "cdi_identifier",
            'C_ORIGINATOR_EDMO_COUNTRY': "c_originator_edmo_country",
            'START_DATE': "start_date",
            'END_DATE': "end_date",
            'C_INSTRUMENT_L05': "c_instrument_l05",
            'VERSION': "version",
            'DATA_FORMAT_L24': "data_format_l24",
            'BBOX_NORTH': "bbox_north",
            'BBOX_EAST': "bbox_east",
            'BBOX_SOUTH': "bbox_south",
            'BBOX_WEST': "bbox_west",
            'C_MEASURING_AREA_TYPE_L02': "c_measuring_area_type_l02",
        },
        ('pagination_sort_type',): {
            'ASC': "asc",
            'DESC': "desc",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'facet_fields': (str,),  # noqa: E501
            'return_fields': (str,),  # noqa: E501
            'pagination_page': (int,),  # noqa: E501
            'pagination_count': (int,),  # noqa: E501
            'pagination_sort': (str,),  # noqa: E501
            'pagination_sort_type': (str,),  # noqa: E501
            'query_fields': (OrderQueryQueryFields,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'facet_fields': 'facet_fields',  # noqa: E501
        'return_fields': 'return_fields',  # noqa: E501
        'pagination_page': 'pagination_page',  # noqa: E501
        'pagination_count': 'pagination_count',  # noqa: E501
        'pagination_sort': 'pagination_sort',  # noqa: E501
        'pagination_sort_type': 'pagination_sort_type',  # noqa: E501
        'query_fields': 'query_fields',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """MetadataQuery - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            facet_fields (str): if multiple options then use comma seperated values, See [reference list facet_fields](https://seadatanet-buffer5.maris.nl/api_v5.1/reference_list/facet_fields). [optional] if omitted the server will use the default value of "parameters_p08,parameters_p03,parameters_p02"  # noqa: E501
            return_fields (str): if multiple options then use comma seperated values, See [reference list return_fields](https://seadatanet-buffer5.maris.nl/api_v5.1/reference_list/return_fields). [optional] if omitted the server will use the default value of "n_code,dataname,cdi_identifier,c_originator_edmo_country,start_date,end_date,c_instrument_l05,version,data_format_l24,bbox_north,bbox_east,bbox_south,bbox_west,c_measuring_area_type_l02"  # noqa: E501
            pagination_page (int): Number of records to return. [optional]  # noqa: E501
            pagination_count (int): Number to start from, never larger then records found. [optional]  # noqa: E501
            pagination_sort (str): Field used for sorting the response, only one value is allowed, See [reference list pagination_sort](https://seadatanet-buffer5.maris.nl/api_v5.1/reference_list/pagination_sort). [optional] if omitted the server will use the default value of "n_code"  # noqa: E501
            pagination_sort_type (str): Field use for sorting the response, only one value is allowed. [optional] if omitted the server will use the default value of "asc"  # noqa: E501
            query_fields (OrderQueryQueryFields): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """MetadataQuery - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            facet_fields (str): if multiple options then use comma seperated values, See [reference list facet_fields](https://seadatanet-buffer5.maris.nl/api_v5.1/reference_list/facet_fields). [optional] if omitted the server will use the default value of "parameters_p08,parameters_p03,parameters_p02"  # noqa: E501
            return_fields (str): if multiple options then use comma seperated values, See [reference list return_fields](https://seadatanet-buffer5.maris.nl/api_v5.1/reference_list/return_fields). [optional] if omitted the server will use the default value of "n_code,dataname,cdi_identifier,c_originator_edmo_country,start_date,end_date,c_instrument_l05,version,data_format_l24,bbox_north,bbox_east,bbox_south,bbox_west,c_measuring_area_type_l02"  # noqa: E501
            pagination_page (int): Number of records to return. [optional]  # noqa: E501
            pagination_count (int): Number to start from, never larger then records found. [optional]  # noqa: E501
            pagination_sort (str): Field used for sorting the response, only one value is allowed, See [reference list pagination_sort](https://seadatanet-buffer5.maris.nl/api_v5.1/reference_list/pagination_sort). [optional] if omitted the server will use the default value of "n_code"  # noqa: E501
            pagination_sort_type (str): Field use for sorting the response, only one value is allowed. [optional] if omitted the server will use the default value of "asc"  # noqa: E501
            query_fields (OrderQueryQueryFields): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
