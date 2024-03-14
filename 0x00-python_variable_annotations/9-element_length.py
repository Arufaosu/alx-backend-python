#!/usr/bin/env python3
"""9-element_length.py"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples containing each element of the input list and its length"""
    return [(i, len(i)) for i in lst]
