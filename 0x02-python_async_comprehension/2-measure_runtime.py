 #!/usr/bin/env python3
import asyncio
from 1-async_comprehension import async_comprehension

# Coroutine to measure the runtime of running async_comprehension four times in parallel
async def measure_runtime():
    """Measure the time it takes to run async_comprehension 4 times in parallel."""
    start_time = asyncio.get_event_loop().time()  # Get start time
    # Run 4 async comprehensions in parallel using asyncio.gather
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = asyncio.get_event_loop().time()  # Get end time
    return end_time - start_time  # Return the time difference