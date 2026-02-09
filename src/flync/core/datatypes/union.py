"""defines a union"""

from typing import TYPE_CHECKING, Annotated, List, Literal

from pydantic import Field, field_validator

from .base import Datatype

if TYPE_CHECKING:
    from . import AllTypes


class UnionMember(Datatype):
    """
    Represents a single member entry of an union datatype.

    Each union member defines a possible datatype that may be present,
    together with its selector index and a descriptive name.

    Parameters
    ----------
    type : AllTypes
        Member datatype (discriminated by its ``type`` field).

    index : int
        Index of the union member. This value is used in the serialized
        union to indicate which member is currently active. Must be
        greater than or equal to 0.

    name : str
        Name of the union member.
    """

    type: Annotated[
        "AllTypes",
        Field(
            description="member datatype (discriminated by its 'type' field)"
        ),
    ]
    index: Annotated[
        int, Field(description="index of the union member", strict=True, ge=0)
    ]
    name: Annotated[str, Field(description="name of the union member")]

    @field_validator("type", mode="before")
    def _wrap_string_type(cls, v):
        if isinstance(v, str):
            s = v.strip().lower()
            return {"type": s}
        return v


class Union(Datatype):
    """
    Represents an union datatype.

    A union allows exactly one of several possible member datatypes to be
    encoded at runtime. The active member is identified using a type
    selector field.

    Parameters
    ----------
    type : Literal["union"]
        Discriminator used to identify this datatype.

    members : list of :class:`UnionMember`
        List of the allowed datatypes a union can contain.

    bit_alignment : Literal[8, 16, 32, 64, 128, 256], optional
        Defines the optional alignment padding that can be added after the
        union to fix the alignment of the next parameter to 8, 16, 32, 64,
        128 or 256 bits.

    length_of_length_field : Literal[0, 8, 16, 32], optional
        Defines the length of the length-field in bits for the union.

    length_of_type_field : Literal[0, 8, 16, 32], optional
        Defines the length of the type-selector field in bits for the union.
    """

    type: Literal["union"] = Field("union")
    members: List[UnionMember] = Field(
        description="list of the allowed datatypes a union can have"
    )
    bit_alignment: Literal[8, 16, 32, 64, 128, 256] = Field(
        default=8,
        description="defines the optional alignment padding that can be \
            added after union to fix the alignment of the next parameter \
                to 8, 16, 32, 64, 128 or 256 bits.",
    )
    length_of_length_field: Literal[0, 8, 16, 32] = Field(
        default=32,
        description="defines the length of the length-field \
            in bits for the union",
    )
    length_of_type_field: Literal[0, 8, 16, 32] = Field(
        default=32,
        description="defines the length of the type-selector-field \
            in bits for the union",
    )
