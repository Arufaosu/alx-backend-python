#!/usr/bin/env python3
import asyncio
from typing import Callable
from asyncio import Task
"""3-tasks.py"""

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> Task:
    """takes an int max_delay"""
    return asyncio.create_task(wait_random(max_delay))

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

if __name__ == "__main__":
    asyncio.run(test(5))
