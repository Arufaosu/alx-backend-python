#!/usr/bin/env python3
"""2-measure_runtime.py"""
import asyncio
from time import perf_counter_ns

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    """measure the total runtime"""
    start_time = perf_counter_ns()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = perf_counter_ns()
    total_runtime = (end_time - start_time) / 1e9
    return total_runtime

async def main():
    return await measure_runtime()

print(asyncio.run(main()))
