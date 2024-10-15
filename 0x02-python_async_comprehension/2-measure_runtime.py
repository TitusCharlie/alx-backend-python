#!/usr/bin/env python3
"""
This module contains the measure_runtime coroutine which measures the time it
takes to run async comprehensions in parallel.
"""
import asyncio
from typing import List
from .async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime for executing async_comprehension 4 times in parallel.
    
    Returns:
        The total time it took to complete the execution.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
