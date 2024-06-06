#!/usr/bin/env python3
"""A module that utilizes type-annotated function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        A type-annotated function make_multiplier that takes a float
        multiplier as argument and returns a function that multiplies
        a float by multiplier.
    """
    def func_mltp(val: float) -> float:
        """
            A nested function that multiplies the function value multiplier
            and val.
        """
        return val * multiplier
    return func_mltp
