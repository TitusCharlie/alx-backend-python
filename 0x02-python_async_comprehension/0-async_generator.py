#!/usr/bin/env python3
"""This module contains the async_generator coroutine."""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Asynchronously generates 10 random numbers between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)  # Wait 1 second asynchronously
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
