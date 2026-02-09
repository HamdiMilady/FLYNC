"""contains definition types for arrays"""

from typing import TYPE_CHECKING, List, Literal, Optional

from pydantic import Field

from flync.core.base_models import FLYNCBaseModel

from .base import ComplexDatatype

if TYPE_CHECKING:
    from . import AllTypes


class ArrayType(ComplexDatatype):
    """
    Generic multidimensional array type.

    Parameters
    ----------
    type : Literal["array"]
        Discriminator identifying this datatype as an array.

    dimensions : List[:class:`ArrayDimension`]
        Ordered list of array dimensions (outer → inner). Must contain
        at least one dimension.

    element_type : :class:`AllTypes`
        Datatype of the innermost array element. This may itself be a
        primitive, struct, union, or another array type.
    """

    type: Literal["array"] = Field("array")
    dimensions: List["ArrayDimension"] = Field(
        min_length=1,
        description="Ordered list of array dimensions (outer → inner)",
    )
    element_type: "AllTypes" = Field(
        description="Datatype of the innermost array element"
    )


class ArrayDimension(FLYNCBaseModel):
    """
    Describes a single array dimension.

    Parameters
    ----------
    kind : Literal["fixed", "dynamic"]
        Specifies whether the dimension has a fixed size or a dynamically
        encoded length.

    length : int, optional
        Number of elements for a fixed-length dimension. Must be greater
        than 0. Only valid when ``kind="fixed"``.

    length_of_length_field : Literal[0, 8, 16, 32], optional
        Size in bits of the length field that precedes the array data for a
        dynamic dimension. Only valid when ``kind="dynamic"``.

    upper_limit : int, optional
        Upper bound on the number of elements. Must be greater than 0.

    lower_limit : int, optional
        Lower bound on the number of elements. Must be greater than or
        equal to 0.

    bit_alignment : Literal[8, 16, 32, 64, 128, 256], optional
        Optional padding alignment in bits applied after this dimension.
    """

    kind: Literal["fixed", "dynamic"]
    # Fixed-length dimension
    length: Optional[int] = Field(
        default=None,
        gt=0,
        description="Number of elements for fixed-length dimension",
    )
    # Dynamic-length dimension
    length_of_length_field: Optional[Literal[0, 8, 16, 32]] = Field(
        default=None,
        description="Length of length-field in bits for dynamic dimension",
    )  # TODO: Validator for dynamic array > 0 and fixed array can be 0
    upper_limit: Optional[int] = Field(
        default=None, gt=0, description="Upper bound of elements"
    )
    lower_limit: Optional[int] = Field(
        default=None, ge=0, description="Lower bound of elements"
    )
    bit_alignment: Optional[Literal[8, 16, 32, 64, 128, 256]] = Field(
        default=None,
        description="Optional padding alignment after this dimension",
    )
