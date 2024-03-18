#!/usr/bin/env python3
import asyncio
import random
from typing import List, Callable
from asyncio import Task
"""4-tasks.py"""

async def wait_random(max_delay: int) -> float:
    """waits for a random delay between 0 and max_delay seconds and returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

def task_wait_random(max_delay: int) -> Task:
    """takes an int max_delay and returns an asyncio"""
    return asyncio.create_task(wait_random(max_delay))

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawns task_wait_random n times with the specified max_delay"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
