"""defines a SOME/IP enum"""

from typing import TYPE_CHECKING, ClassVar, List, Literal, Union

from pydantic import BaseModel, Field, ValidationInfo, field_validator

from flync.core.utils.exceptions import err_minor

from .base import Datatype
from .primitive import UInt8

if TYPE_CHECKING:
    from . import Ints


class EnumEntry(BaseModel):
    """
    Represents a single entry in an enumeration.

    Parameters
    ----------
    value : int
        Numeric value associated with the enumeration entry.

    name : str
        Symbolic name of the enumeration entry.

    description : str, optional
        Human-readable description of the enumeration entry.
    """

    value: int = Field()
    name: str = Field()
    description: str = Field("")


class Enum(Datatype):
    """
    Allows modeling SOME/IP enumerations with value, name, and description.

    Parameters
    ----------
    name : str
        Unique name of the datatype.

    description : str, optional
        Human-readable description of the datatype.

    type : Literal["enum"]
        Datatype discriminator identifying this datatype as an enumeration.

    endianness : Literal["BE", "LE"], optional
        Byte order used for encoding multi-byte values. Defaults to
        big-endian ("BE").

    base_type : Ints, optional
        Underlying integer datatype used to encode enumeration values.
        Defaults to :class:`UInt8`.

    entries : list of :class:`EnumEntry`, optional
        List of enumeration entries defining the mapping between numeric
        values and symbolic names.
    """

    type: Literal["enum"] = Field("enum")
    base_type: Union["Ints"] = Field(
        default_factory=lambda: Enum.default_base_type()
    )
    entries: List[EnumEntry] = Field(default_factory=list)
    BASE_TYPE_RANGES: ClassVar[dict[str, tuple[int, int]]] = {
        "UInt8": (0, 2**8 - 1),
        "UInt16": (0, 2**16 - 1),
        "UInt32": (0, 2**32 - 1),
        "UInt64": (0, 2**64 - 1),
        "SInt8": (-(2**7), 2**7 - 1),
        "SInt16": (-(2**15), 2**15 - 1),
        "SInt32": (-(2**31), 2**31 - 1),
        "SInt64": (-(2**63), 2**63 - 1),
    }

    @field_validator("entries")
    @classmethod
    def validate_entries(
        cls, entries: list["EnumEntry"], info: ValidationInfo
    ) -> list["EnumEntry"]:
        base_type = info.data.get("base_type")
        if base_type is None:
            return entries  # Cannot validate without base_type
        base_type_name = base_type.__class__.__name__
        min_value, max_value = cls.BASE_TYPE_RANGES[base_type_name]
        seen = set()
        for entry in entries:
            if entry.value in seen:
                raise err_minor(f"Duplicate enum value: {entry.value}")
            seen.add(entry.value)
            if not (min_value <= entry.value <= max_value):
                raise err_minor(
                    f"Enum value {entry.value} "
                    f"exceeds valid range for {base_type_name} "
                    f"({min_value} to {max_value})"
                )
        return entries

    @staticmethod
    def default_base_type() -> UInt8:
        return UInt8(type="uint8", endianness="LE", signed=False, bit_size=8)
