#!/usr/bin/env python3
"""2-measure_runtime.py"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """measure the total runtime"""
    starttime = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    totaltime = time.time() - starttime
    return totaltime
