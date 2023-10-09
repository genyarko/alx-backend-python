#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
  """Waits for a random delay between 0 and max_delay seconds and eventually returns it.

  Args:
    max_delay: The maximum delay in seconds.

  Returns:
    A float value representing the random delay in seconds.
  """

  delay = random.uniform(0, max_delay)
  await asyncio.sleep(delay)
  return delay
