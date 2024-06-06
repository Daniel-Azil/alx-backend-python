#!/usr/bin/env python3
"""A module that utilizes type-annotated function."""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        A function that return a list containing tuple.
    """
    return [(i, len(i)) for i in lst]
