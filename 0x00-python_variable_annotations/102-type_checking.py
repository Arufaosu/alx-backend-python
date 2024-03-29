#!/usr/bin/env python3
"""102-type_checking.py"""

from typing import List, Tuple

def zoom_array(lst: List, factor: int = 2) -> List:
    """uses mypy to validate the code and make changes"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
