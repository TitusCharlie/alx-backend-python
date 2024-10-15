#!/usr/bin/env python3
"""
This module contains the async_comprehension coroutine which collects
random numbers using an async generator.
"""
from typing import List
from .async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension.
    
    Returns:
        A list of 10 random floating-point numbers.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
