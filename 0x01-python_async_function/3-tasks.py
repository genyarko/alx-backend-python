#!/usr/bin/env python3
"""
Task 3's module.
"""

import asyncio

ait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine with the given max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio.Task representing the execution of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
