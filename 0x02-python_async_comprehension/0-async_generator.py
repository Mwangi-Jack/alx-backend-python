#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
    this async generator loops 10 time, each time
    asynchronously waiting for 1 sec and yielding a random number
    between 0 and 10
    """

    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
