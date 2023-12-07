#!/usr/bin/env python3
"""
Module that sums elements of a list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    takes a list of floats and returns the sum
    Args:
        input_list: a list of floats
    Return:
        the sum as a float
    """
    total: float = 0.0

    for item in input_list:
        total += item

    return total
