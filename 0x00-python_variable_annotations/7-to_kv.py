#!/usr/bin/env python3

"""String and int/float to tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This functioin takes in string and an int/float variables
     and returns a tuple of the two
    """
    return (k, v)
