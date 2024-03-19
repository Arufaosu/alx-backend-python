#!/usr/bin/env python3
"""0-async_generator.py"""
import asyncio
import random

async def async_generator():
    """ loop 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def main():
    async for num in async_generator():
        print(num)

asyncio.run(main())
