#!/usr/bin/env python3
"""Duck typing using TypeVar"""

from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    This function takes in a dictionary, a key and a default varibale 'default'
    and returns the value of the given key in the dict or None
    """
    if key in dct:
        return dct[key]
    else:
        return default

