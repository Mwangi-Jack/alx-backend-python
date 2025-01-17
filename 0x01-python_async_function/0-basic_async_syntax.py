#!/usr/bin/env python3
"""Basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This asynchronous coroutine function takes an integer argument
    'max_delay' with a default value of 10 and awaits a random delay
    between 0 and 'max_delay' seconds and returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
