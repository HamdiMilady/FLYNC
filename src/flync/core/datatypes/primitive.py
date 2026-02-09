"""contains the primitive datatypes"""

from typing import Annotated, ClassVar, Literal

from pydantic import Field

from .base import PrimitiveDatatype


class Boolean(PrimitiveDatatype):
    """
    Boolean primitive datatype.

    Parameters
    ----------
    name : str
        Datatype name. Defaults to ``"BOOLEAN"``.

    type : Literal["boolean"]
        Discriminator identifying the primitive boolean datatype.
    """

    name: str = Field(default="BOOLEAN")
    type: Literal["boolean"] = Field("boolean")


class BaseInt(PrimitiveDatatype):
    """
    Base class for all integer primitive datatypes.

    This class provides shared semantics for signed and unsigned integer
    representations and defines common descriptive metadata.

    """

    MAX_APPLICATIVE_VALUE_DESC: ClassVar[str] = (
        "the maximum value to define by application"
    )


class BaseFloat(PrimitiveDatatype):
    """
    Base class for all floating-point primitive datatypes.

    This class provides shared semantics for floating-point representations
    and defines common descriptive metadata.

    """

    MAX_APPLICATIVE_VALUE_DESC: ClassVar[str] = (
        "the maximum value to define by application"
    )


class UInt8(BaseInt):
    """
    Unsigned 8-bit integer datatype.

    Parameters
    ----------
    name : str
        Datatype name. Defaults to ``"UINT_8"``.

    type : Literal["uint8"]
        Discriminator identifying this datatype.

    signed : Literal[False]
        Indicates that the integer is unsigned.

    bit_size : int
        Storage size in bits. Defaults to 8.

    max_applicative_value : int
        Maximum application-level value allowed for this datatype.
    """

    name: str = Field(default="UINT_8")
    type: Literal["uint8"] = Field("uint8")  # type: ignore
    signed: Literal[False] = Field(False)
    bit_size: Annotated[int, Field(gt=0, le=8, default=8)]
    max_applicative_value: Annotated[int, Field(ge=0, le=255)] = Field(
        description=BaseInt.MAX_APPLICATIVE_VALUE_DESC, default=255
    )  # type: ignore


class UInt16(BaseInt):
    """
    Unsigned 16-bit integer datatype.

    Parameters
    ----------
    name : str
        Datatype name. Defaults to ``"UINT_16"``.

    type : Literal["uint16"]
        Discriminator identifying this datatype.

    signed : Literal[False]
        Indicates that the integer is unsigned.

    bit_size : int
        Storage size in bits. Defaults to 16.

    max_applicative_value : int
        Maximum application-level value allowed for this datatype.
    """

    name: str = Field(default="UINT_16")

    type: Literal["uint16"] = Field("uint16")  # type: ignore
    signed: Literal[False] = Field(False)
    bit_size: Annotated[int, Field(gt=8, le=16, default=16)]
    max_applicative_value: Annotated[int, Field(ge=0, le=65535)] = Field(
        description=BaseInt.MAX_APPLICATIVE_VALUE_DESC, default=65535
    )


class UInt32(BaseInt):
    """
    Unsigned 32-bit integer datatype.

    Parameters
    ----------
    name : str
        Datatype name. Defaults to ``"UINT_32"``.

    type : Literal["uint32"]
        Discriminator identifying this datatype.

    signed : Literal[False]
        Indicates that the integer is unsigned.

    bit_size : int
        Storage size in bits. Defaults to 32.

    max_applicative_value : int
        Maximum application-level value allowed for this datatype.
    """

    name: str = Field(default="UINT_32")
    type: Literal["uint32"] = Field("uint32")  # type: ignore
    signed: Literal[False] = Field(False)
    bit_size: Annotated[int, Field(gt=16, le=32, default=32)]
    max_applicative_value: Annotated[int, Field(ge=0, le=4294967295)] = Field(
        description=BaseInt.MAX_APPLICATIVE_VALUE_DESC, default=4294967295
    )


class UInt64(BaseInt):
    """
    Unsigned 64-bit integer datatype.

    Parameters
    ----------
    name : str
        Datatype name. Defaults to ``"UINT_64"``.

    type : Literal["uint64"]
        Discriminator identifying this datatype.

    signed : Literal[False]
        Indicates that the integer is unsigned.

    bit_size : int
        Storage size in bits. Defaults to 64.

    max_applicative_value : int
        Maximum application-level value allowed for this datatype.
    """

    name: str = Field(default="UINT_64")
    type: Literal["uint64"] = Field("uint64")  # type: ignore
    signed: Literal[False] = Field(False)
    bit_size: Annotated[int, Field(gt=32, le=64, default=64)]
    max_applicative_value: Annotated[int, Field(ge=0, le=2**64)] = Field(
        description=BaseInt.MAX_APPLICATIVE_VALUE_DESC, default=2**64
    )


class SInt8(BaseInt):
    """
    Signed 8-bit integer datatype.

    Parameters
    ----------
    name : str
        Datatype name. Defaults to ``"SINT_8"``.

    type : Literal["sint8"]
        Discriminator identifying this datatype.

    signed : Literal[True]
        Indicates that the integer is signed.

    bit_size : int
        Storage size in bits. Defaults to 8.

    max_applicative_value : int
        Maximum application-level value allowed for this datatype.
    """

    name: str = Field(default="SINT_8")
    type: Literal["sint8"] = Field("sint8")  # type: ignore
    signed: Literal[True] = Field(True)
    bit_size: Annotated[int, Field(gt=0, le=8, default=8)]
    max_applicative_value: Annotated[int, Field(ge=-128, le=127)] = Field(
        description=BaseInt.MAX_APPLICATIVE_VALUE_DESC, default=127
    )


class SInt16(BaseInt):
    """
    Signed 16-bit integer datatype.

    Parameters
    ----------
    name : str
        Datatype name. Defaults to ``"SINT_16"``.

    type : Literal["sint16"]
        Discriminator identifying this datatype.

    signed : Literal[True]
        Indicates that the integer is signed.

    bit_size : int
        Storage size in bits. Defaults to 16.

    max_applicative_value : int
        Maximum application-level value allowed for this datatype.
    """

    name: str = Field(default="SINT_16")
    type: Literal["sint16"] = Field("sint16")  # type: ignore
    signed: Literal[True] = Field(True)
    bit_size: Annotated[int, Field(gt=8, le=16, default=16)]
    max_applicative_value: Annotated[int, Field(ge=-32768, le=32767)] = Field(
        description=BaseInt.MAX_APPLICATIVE_VALUE_DESC, default=32767
    )


class SInt32(BaseInt):
    """
    Signed 32-bit integer datatype.

    Parameters
    ----------
    name : str
        Datatype name. Defaults to ``"SINT_32"``.

    type : Literal["sint32"]
        Discriminator identifying this datatype.

    signed : Literal[True]
        Indicates that the integer is signed.

    bit_size : int
        Storage size in bits. Defaults to 32.

    max_applicative_value : int
        Maximum application-level value allowed for this datatype.
    """

    name: str = Field(default="SINT_32")
    type: Literal["sint32"] = Field("sint32")  # type: ignore
    signed: Literal[True] = Field(True)
    bit_size: Annotated[int, Field(gt=16, le=32, default=32)]
    max_applicative_value: Annotated[
        int, Field(ge=-2147483648, le=2147483647)
    ] = Field(
        description=BaseInt.MAX_APPLICATIVE_VALUE_DESC, default=2147483647
    )


class SInt64(BaseInt):
    """
    Signed 64-bit integer datatype.

    Parameters
    ----------
    name : str
        Datatype name. Defaults to ``"SINT_64"``.

    type : Literal["sint64"]
        Discriminator identifying this datatype.

    signed : Literal[True]
        Indicates that the integer is signed.

    bit_size : int
        Storage size in bits. Defaults to 64.

    max_applicative_value : int
        Maximum application-level value allowed for this datatype.
    """

    name: str = Field(default="SINT_64")
    type: Literal["sint64"] = Field("sint64")  # type: ignore
    signed: Literal[True] = Field(True)
    bit_size: Annotated[int, Field(gt=32, le=64, default=64)]
    max_applicative_value: Annotated[
        int, Field(ge=-9223372036854775808, le=9223372036854775807)
    ] = Field(
        description=BaseInt.MAX_APPLICATIVE_VALUE_DESC,
        default=9223372036854775807,
    )


class Float32(PrimitiveDatatype):
    """
    32-bit floating-point datatype.

    Parameters
    ----------
    name : str
        Datatype name. Defaults to ``"FLOAT_32"``.

    type : Literal["float32"]
        Discriminator identifying this datatype.

    max_applicative_value : float
        Maximum application-level absolute value allowed.
    """

    name: str = Field(default="FLOAT_32")
    type: Literal["float32"] = Field("float32")  # type: ignore
    max_applicative_value: Annotated[
        float, Field(ge=-3.4028235e38, le=3.4028235e38)
    ] = Field(description=BaseFloat.MAX_APPLICATIVE_VALUE_DESC, default=3.4e38)


class Float64(BaseFloat):
    """
    64-bit floating-point datatype.

    Parameters
    ----------
    name : str
        Datatype name. Defaults to ``"FLOAT_64"``.

    type : Literal["float64"]
        Discriminator identifying this datatype.

    bit_size : int
        Storage size in bits. Defaults to 64.

    max_applicative_value : float
        Maximum application-level absolute value allowed.
    """

    name: str = Field(default="FLOAT_64")
    type: Literal["float64"] = Field("float64")  # type: ignore
    bit_size: Annotated[int, Field(ge=33, le=64, default=64)]
    max_applicative_value: Annotated[
        float,
        Field(ge=-1.7976931348623157e308, le=1.7976931348623157e308),
    ] = Field(
        description=BaseFloat.MAX_APPLICATIVE_VALUE_DESC,
        default=1.7976931348623157e308,
    )
