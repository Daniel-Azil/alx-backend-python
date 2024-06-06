#!/usr/bin/env python3
"""A module that utilizes type-annotated function."""
from typing import Union, Mapping, Any, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
        A function that returns value of the given dictionary
        key if found, else returns the default argument passed.
    """
    if key in dct:
        return dct[key]
    else:
        return default
