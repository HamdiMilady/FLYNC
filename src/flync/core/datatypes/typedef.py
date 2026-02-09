"""contains the definition types for typedef"""

from typing import TYPE_CHECKING, Literal

from pydantic import Field

from .base import ComplexDatatype

if TYPE_CHECKING:
    from . import AllTypes


class Typedef(ComplexDatatype):
    """
    Alias datatype that references another datatype definition.

    A typedef introduces an alternative name for an existing datatype
    without changing its underlying structure or serialization behavior.

    Parameters
    ----------
    type : Literal["typedef"]
        Discriminator used to identify this datatype.

    name : str
        Name of the typedef reference.

    datatyperef : AllTypes
        Referenced datatype definition that this typedef aliases.
    """

    type: Literal["typedef"] = Field("typedef")
    name: str = Field(description="Name of the typedef reference")
    datatyperef: "AllTypes" = Field(
        description="Referenced datatype definition"
    )  # type: ignore
