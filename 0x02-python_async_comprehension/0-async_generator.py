#!/usr/bin/env python3
"""
This module contains the async_generator coroutine which asynchronously yields
random numbers.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generates 10 random numbers between 0 and 10 asynchronously, yielding
    one number per second.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait 1 second asynchronously
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
