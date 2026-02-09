from typing import Iterable, Optional, TypeVar

T = TypeVar("T")


def get_metadata(meta: Iterable[object], cls: type[T]) -> Optional[T]:
    """"""
    for m in meta:
        if isinstance(m, cls):
            return m
    return None


def get_name(named_object: T, fallback_name: str | None = None) -> str:
    return (
        getattr(named_object, "name", fallback_name)
        or type(named_object).__name__
    )
