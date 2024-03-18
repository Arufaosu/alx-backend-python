#!/usr/bin/env python3
from typing import List
import time
import asyncio
import random
"""2-measure_runtime.py"""

async def wait_random(max_delay: int) -> float:
    """waits for a random delay between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait_random n times with the specified max_delay"""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)

def measure_time(n: int, max_delay: int) -> float:
    """measure the total execution time for wait_n(n, max_delay)"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
