#!/usr/bin/env python3
"""
Module that measures the runtime of a concurrent process
"""
from time import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns the maximum time taken to perform the operation
    """
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()

    return (end - start) / n
