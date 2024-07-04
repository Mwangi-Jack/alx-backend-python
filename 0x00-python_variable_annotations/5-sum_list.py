#!/usr/bin/env python3
"""List type annotation"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes in a list of float elements
    and returns their sum
    """
    sum: float = 0

    for val in input_list:
        sum += val

    return sum
