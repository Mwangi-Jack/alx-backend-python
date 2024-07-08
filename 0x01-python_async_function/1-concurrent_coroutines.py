#!/usr/bin/env python3
"""executing multiple coroutines at the same time -concurrency"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function takes in two intager  arguments
    'n' and 'max_delay' and returns a list of all delays
    called with the 'wait_random' function
    """

    tasks = [wait_random(max_delay) for _ in range(n)]

    li = [await task for task in asyncio.as_completed(tasks)]

    return li
