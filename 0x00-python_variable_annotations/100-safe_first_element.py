#!/usr/bin/env python3
"""A module that utilizes type-annotated function."""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        A funtion that returns the first element in the sequence
        if found, else returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
