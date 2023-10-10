#!/usr/bin/env python3
"""
Async comprehension coroutine that collects 10 random numbers.
"""

import asyncio

from 0-async_generator import async_generator  # Import the previously defined async_generator coroutine

async def async_comprehension() -> List[float]:
    """
    An asynchronous coroutine that collects 10 random numbers using async comprehension.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [num async for num in async_generator()]
