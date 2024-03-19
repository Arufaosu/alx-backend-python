#!/usr/bin/env python3
"""1-async_comprehension.py"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """collects 10 random numbers"""
    return [Num async for Num in async_generator()]
