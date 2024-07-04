#!/usr/bin/python3

"""type annotated function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    this function takes a mixed list of either float
    or integer values and returns their sum (type float)
    """
    sum: float = 0

    for val in mxd_lst:
        sum += val

    return sum
