#!/usr/bin/env python3
"""Duck typing"""

from types import NoneType
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """Duck typing"""
    if lst:
        return lst[0]
    else:
        return None
