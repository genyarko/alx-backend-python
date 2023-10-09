#!/usr/bin/env python3
"""
Task 4's module.
"""

import asyncio
from typing import List

from 0-basic_async_syntax import wait_random
from 3-tasks import task_wait_random  # Import the previously defined task_wait_random function

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays (float values) in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    await asyncio.gather(*tasks)
    return [task.result() for task in tasks]

if __name__ == "__main__":
    import asyncio

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
