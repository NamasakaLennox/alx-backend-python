#!/usr/bin/env python3
"""
A module that handles a mixed annotation type
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    adds all values in a list of integers and floats
    Args:
        mxd_lst: a list of integers and floats
    Return:
        the sum of all elements as a float
    """
    total: float = 0

    for item in mxd_lst:
        total += item

    return total
