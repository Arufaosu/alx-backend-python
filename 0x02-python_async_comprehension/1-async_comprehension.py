#!/usr/bin/env python3
"""1-async_comprehension.py"""
import asyncio
from typing import Generator
import random

async def async_comprehension() -> Generator[float, None, None]:
    """collects 10 random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
