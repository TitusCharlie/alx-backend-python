#!/usr/bin/env python3
"""This module contains the async_comprehension coroutine."""
from typing import List
from .async_generator import async_generator

async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from async_generator using async for."""
    result = []
    async for i in async_generator():
        result.append(i)
    return result

    # return [i async for i in async_generator()]  # List comprehension to collect random numbers
