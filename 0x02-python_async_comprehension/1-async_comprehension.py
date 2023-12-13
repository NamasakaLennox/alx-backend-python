#!/usr/bin/env python3
"""
collects 10 random numbers and returns them
"""
from random import random
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects random numbers and returns a list of those numbers
    """
    return [i async for i in async_generator()]
