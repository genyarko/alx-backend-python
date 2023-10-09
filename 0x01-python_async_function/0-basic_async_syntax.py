#!/usr/bin/env python3
"""
Async coroutine that waits for a random delay and returns it.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive) seconds.

    Args:
        max_delay (int, optional): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay in seconds.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
