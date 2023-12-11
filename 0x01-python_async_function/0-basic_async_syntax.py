#!/usr/bin/env python3
"""
writing an asyncronous coroutine
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    delays an operation for a given time and returns the value
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
