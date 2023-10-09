#!/usr/bin/env python3
"""
Task 1's module.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays (float values) in ascending order.
    """
    wait_times = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(wait_times)
