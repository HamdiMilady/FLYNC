from pydantic import Field

from .base import ComplexDatatype


class ValueTable(ComplexDatatype):
    """
    Represents a table of values with an associated description.

    Parameters
    ----------
    num_value : int
        The numeric value associated with this table entry.

    description : str
        Human-readable description of the table entry.
    """

    num_value: int = Field()
    description: str = Field()
