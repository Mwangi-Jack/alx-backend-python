#!/usr/bin/env python3

"""Duck typing an iterable object"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function takes in a list"""
    return [(i, len(i)) for i in lst]
