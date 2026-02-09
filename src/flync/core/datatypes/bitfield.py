"""defines a SOME/IP BitField"""

from typing import List, Literal, Optional

from pydantic import BaseModel, Field, model_validator

from flync.core.utils.exceptions import err_minor

from .base import Datatype


class BitfieldEntryValue(BaseModel):
    """
    Represents a named value within a bitfield entry.

    Parameters
    ----------
    value : int
        Numeric value represented by this bitfield entry value.

    name : str
        Symbolic name associated with the value.

    description : str, optional
        Human-readable description of the value.
    """

    value: int = Field()
    name: str = Field()
    description: Optional[str] = Field("", description="Optional description")


class BitfieldEntry(BaseModel):
    """
    Describes a single field within a bitfield.

    Parameters
    ----------
    name : str
        Name of the individual bitfield.

    bitposition : int
        Bit position of the individual bitfield within the enclosing
        bitfield datatype.

    description : str, optional
        Human-readable description of the field.

    values : list of :class:`BitfieldEntryValue`, optional
        Optional enumeration of named values defined for this bitfield
        entry.
    """

    name: str = Field(..., description="Name of the individual bitfield")
    bitposition: int = Field(
        ..., description="Bitposition for the individual bitfield"
    )
    description: Optional[str] = Field(
        "", description="Optional description of the field"
    )
    values: Optional[List[BitfieldEntryValue]] = Field(
        default_factory=list,
        description="Optional values defined for the entry",
    )


class Bitfield(Datatype):
    """
    Allows modeling of SOME/IP bitfields.

    Parameters
    ----------
    name : str
        Unique name of the datatype.

    description : str, optional
        Human-readable description of the datatype.

    type : Literal["bitfield"]
        Discriminator identifying this datatype as a bitfield.

    endianness : Literal["BE", "LE"], optional
        Byte order used for encoding multi-byte values. Defaults to
        big-endian ("BE").

    length : Literal[8, 16, 32, 64], optional
        Size of the bitfield in bits.

    fields : list of :class:`BitfieldEntry`
        List of bitfield entries that define the individual bit ranges.
    """

    type: Literal["bitfield"] = Field("bitfield")

    length: Literal[8, 16, 32, 64] = Field(
        default=8,
        description="defines the possible length of the bitfield",
    )

    fields: Optional[List[BitfieldEntry]] = Field(
        default=None, description="List of bitfield entries"
    )

    @model_validator(mode="after")
    def validate_length_against_fields_size(self):
        """Validate size of fields equals bitfield length"""
        if self.fields is not None and len(self.fields) <= self.length:
            err_minor(
                f"Mismatch between length({self.length}) and "
                f"number of defined fields ({len(self.fields)})"
            )
        return self

    @model_validator(mode="after")
    def validate_bitfieldposition_of_entries(self):
        """Validate bitfield position for all entries must be in range"""
        if self.fields is not None:
            for field in self.fields:
                if field.bitposition < self.length:
                    err_minor(
                        f"Bitposition of {field.name} is out of range: "
                        f"{field.bitposition} >= {self.length}"
                    )
        return self
