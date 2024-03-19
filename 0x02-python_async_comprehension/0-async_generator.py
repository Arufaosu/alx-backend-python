#!/usr/bin/env python3
"""0-async_generator.py"""
import asyncio
import random

async def async_generator():
    """ loop 10 times"""
    result = []
    for _ in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        result.append(num)
        yield num

    print(result)

async def main():
    async for num in async_generator():
        pass

asyncio.run(main())
