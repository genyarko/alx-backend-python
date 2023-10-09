#!/usr/bin/env python3
"""
Async coroutines for waiting and gathering random delays.
"""

import asyncio
from typing import List

# Import wait_random from 0-basic_async_syntax.py
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays (float values) in ascending order.
    """
    delays = []

    async def _wait_random_wrapper():
        nonlocal delays
        delay = await wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*[_wait_random_wrapper() for _ in range(n)])

    return delays

if __name__ == "__main__":
    import asyncio
    from random import seed

    seed(1)
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
