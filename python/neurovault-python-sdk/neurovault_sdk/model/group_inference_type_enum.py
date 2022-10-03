# coding: utf-8

"""
    Neurovault API

    All ur images r belong to us  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from neurovault_sdk import schemas  # noqa: F401


class GroupInferenceTypeEnum(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "randommixedeffects": "RANDOMMIXEDEFFECTS",
            "fixedeffects": "FIXEDEFFECTS",
        }
    
    @schemas.classproperty
    def RANDOMMIXEDEFFECTS(cls):
        return cls("randommixedeffects")
    
    @schemas.classproperty
    def FIXEDEFFECTS(cls):
        return cls("fixedeffects")
