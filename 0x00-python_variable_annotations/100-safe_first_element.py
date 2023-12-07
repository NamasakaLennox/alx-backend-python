#!/usr/bin/env python3
"""
augment the given code
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """
    returns the correct duck type notations
    """
    if lst:
        return lst[0]
    else:
        return None
