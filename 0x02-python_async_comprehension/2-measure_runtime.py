#!/usr/bin/env python3
"""
measure the total runtime of 4 async functions and returns value
"""
from asyncio import create_task, gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures runtime for 4 parallel processes and returns the total time taken
    """
    start = time()
    res = await gather(async_comprehension(),
                       async_comprehension(),
                       async_comprehension(),
                       async_comprehension())
    end = time()
    return end - start
