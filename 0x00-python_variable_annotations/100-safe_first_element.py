#!/usr/bin/env python3
"""100-safe_first_element.py"""

from typing import Sequence, Any, Union, Optional

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of a sequence if it exists otherwise returns None"""
    if lst:
        return lst[0]
    else:
        return None
