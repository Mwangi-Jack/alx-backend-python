#!/usr/bin/env python3

from types import NoneType
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, NoneType] = None) -> Union[Any, T] :
    """safely get a value"""

    if key in dct:
        return dct[key]
    else:
        return default