#!/usr/bin/env python3
"""
Executing multiple coroutines at the same time using async
"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n times given delay as param
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
