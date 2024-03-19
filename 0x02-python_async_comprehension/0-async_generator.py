#!/usr/bin/env python3
"""0-async_generator.py"""
import asyncio
from typing import AsyncGenerator
import random

async def async_generator() -> AsyncGenerator[float, None]:
    """ loop 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
