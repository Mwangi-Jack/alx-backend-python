#!/usr/bin/env python3

"""Make multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float 'multiplier' as argument
    and returns a function that multiplies a float by 'multiplier'
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
