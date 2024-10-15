#!/usr/bin/env python3
"""This module contains the measure_runtime coroutine."""
import asyncio
from typing import List
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """Measure the runtime of executing async_comprehension 4 times in parallel."""
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
