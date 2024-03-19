#!/usr/bin/env python3
"""0-async_generator.py"""
import asyncio
import random

async def async_generator():
    """ loop 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def print_yielded_values():
    """relies on 0-main"""
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
