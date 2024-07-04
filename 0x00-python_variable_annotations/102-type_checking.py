#!/usr/bin/env python3
"""Type Checking"""

from typing import List, Any

def zoom_array(lst: List[Any], factor: Any = 2) -> List:
    """
    This function takes in two varibales  a tuple 'lst' and
    a integer 'factor'  and returns a tuple
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
