#!/usr/bin/env python3
import asyncio
from typing import List
from random import uniform
from asyncio import gather
"""1-concurrent_coroutines.py"""

async def wait_random(max_delay: int) -> float:
    """ waits for a random delay between 0 and max_delay"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawns wait_random n times with the specified max_delay"""
    delays = await gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)

async def main():
    print(await wait_n(5, 5))
    print(await wait_n(10, 7))
    print(await wait_n(10, 0))

if __name__ == "__main__":
    asyncio.run(main())
