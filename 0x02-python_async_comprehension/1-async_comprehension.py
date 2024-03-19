#!/usr/bin/env python3
"""1-async_comprehension.py"""
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension():
    """collects 10 random numbers"""
    random_numbers = [i async for i in async_generator()]
    return random_numbers

async def main():
    """print result"""
    print(await async_comprehension())

asyncio.run(main())
