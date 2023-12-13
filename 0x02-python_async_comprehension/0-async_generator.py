#!/usr/bin/env python3
"""
loops 10 times and yields a random number between 0 and 10
"""
import asyncio
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    an async generator, yields a value after every loop
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random() * 10
