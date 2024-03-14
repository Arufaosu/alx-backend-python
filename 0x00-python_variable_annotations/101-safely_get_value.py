#!/usr/bin/env python3
"""101-safely_get_value.py"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """returns the value associated with the given key in the dictionary `dct`"""
    if key in dct:
        return dct[key]
    else:
        return default
