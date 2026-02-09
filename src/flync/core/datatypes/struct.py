"""contains the definition types for structs"""

from typing import TYPE_CHECKING, List, Literal

from pydantic import Field

from .base import ComplexDatatype

if TYPE_CHECKING:
    from . import AllTypes


class Struct(ComplexDatatype):
    """
    Structured datatype composed of multiple ordered members.

    A struct groups several datatypes into a single composite element that
    is serialized in the order the members are defined.

    Parameters
    ----------
    type : Literal["struct"]
        Discriminator used to identify this datatype.

    members : List[AllTypes]
        Ordered list of datatypes that form the members of the struct.

    bit_alignment : Literal[8, 16, 32, 64, 128, 256]
        Optional padding alignment applied after the struct to ensure the
        next parameter starts at the specified bit boundary.

    length_of_length_field : Literal[0, 8, 16, 32]
        Size of the optional length field in bits that prefixes the struct.
        A value of 0 indicates that no length field is present.
    """

    type: Literal["struct"] = Field("struct")
    members: List["AllTypes"] = Field(
        description="the members of the struct"
    )  # type: ignore
    bit_alignment: Literal[8, 16, 32, 64, 128, 256] = Field(
        default=8,
        description="defines the optional alignment padding that can be added "
        "after the variable length data element like struct to "
        "fix the alignment of the next parameter to 8, 16, 32, "
        "64, 128, or 256 bits.",
    )
    length_of_length_field: Literal[0, 8, 16, 32] = Field(
        default=0,
        description="defines the length of the length-field in bits for "
        "the struct",
    )
