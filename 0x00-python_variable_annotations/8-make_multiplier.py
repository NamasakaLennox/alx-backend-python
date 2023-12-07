#!/usr/bin/env python3
"""
takes a multiplier and returns a function that multiplies a float
by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float a returns a callable function to multiply the annotations
    with others
    """
    def func(x: float) -> float:
        """
        takes the mutiplier and mutiplies a function with it
        """
        out: float = multiplier * x

        return out

    return func
