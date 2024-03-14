#!/usr/bin/env python3
"""7-to_kv.py"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple with the string k as the first element and square of the int/float v as the second element"""
    return (k, float(v) ** 2)
