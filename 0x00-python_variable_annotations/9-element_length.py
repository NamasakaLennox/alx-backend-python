#!/usr/bin/env python3
"""
Annotate a given function and return values with appropriate types
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns the length of an element
    """
    return [(i, len(i)) for i in lst]
