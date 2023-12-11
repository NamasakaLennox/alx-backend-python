#!/usr/bin/env python3
"""
takes an integer and returns an asyncio.Task
"""
from asyncio import create_task, Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    takes a delay time and creates a task from it
    """
    task = create_task(wait_random(max_delay))

    return (task)
