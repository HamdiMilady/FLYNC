"""this module contains classes to model datatypes for SOME/IP services"""

import typing

import pydantic

from .array import ArrayDimension, ArrayType
from .base import ComplexDatatype, Datatype, PrimitiveDatatype
from .bitfield import Bitfield, BitfieldEntry, BitfieldEntryValue
from .bitrange import BitRange
from .enum import Enum, EnumEntry
from .ipaddress import IPv4AddressEntry, IPv6AddressEntry
from .macaddress import (
    MACAddressEntry,
    MulticastMACAddressEntry,
    UnicastMACAddressEntry,
)
from .primitive import (
    BaseFloat,
    BaseInt,
    Boolean,
    Float32,
    Float64,
    SInt8,
    SInt16,
    SInt32,
    SInt64,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
)
from .string import BaseString, DynamicLengthString, FixedLengthString
from .struct import Struct
from .typedef import Typedef
from .union import Union, UnionMember
from .value_range import ValueRange
from .value_table import ValueTable

SignedInts = typing.Annotated[
    SInt8 | SInt16 | SInt32 | SInt64,
    pydantic.Field(discriminator="type"),
]
"Collection of Signed Integer Types"

UnsignedInts = typing.Annotated[
    UInt8 | UInt16 | UInt32 | UInt64,
    pydantic.Field(discriminator="type"),
]
"Collection of Unsigned Integer Types"

Ints = typing.Annotated[
    SignedInts | UnsignedInts,
    pydantic.Field(discriminator="type"),
]
"Collection of Integer Types"

Floats = typing.Annotated[
    Float32 | Float64,
    pydantic.Field(discriminator="type"),
]
"Collection of Float Types"

AllTypes = typing.Annotated[
    Ints
    | Floats
    | Enum
    | Boolean
    | Struct
    | Union
    | ArrayType
    | DynamicLengthString
    | FixedLengthString
    | Bitfield,
    pydantic.Field(discriminator="type"),
]
"Collection of all dataypes"

__all__ = [
    "Ints",
    "AllTypes",
    "Datatype",
    "PrimitiveDatatype",
    "ComplexDatatype",
    "ArrayType",
    "ArrayDimension",
    "BitfieldEntryValue",
    "BitfieldEntry",
    "Bitfield",
    "BitRange",
    "EnumEntry",
    "Enum",
    "IPv4AddressEntry",
    "IPv6AddressEntry",
    "MACAddressEntry",
    "UnicastMACAddressEntry",
    "MulticastMACAddressEntry",
    "Boolean",
    "BaseInt",
    "UInt8",
    "UInt16",
    "UInt32",
    "UInt64",
    "SInt8",
    "SInt16",
    "SInt32",
    "SInt64",
    "BaseFloat",
    "Floats",
    "Float32",
    "Float64",
    "BaseString",
    "FixedLengthString",
    "DynamicLengthString",
    "Struct",
    "Typedef",
    "UnionMember",
    "Union",
    "ValueRange",
    "ValueTable",
]
