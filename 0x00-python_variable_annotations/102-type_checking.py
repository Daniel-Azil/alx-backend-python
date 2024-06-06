#!/usr/bin/env python3
"""A module that utilizes type-annotated function."""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        A function that returns a list.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
