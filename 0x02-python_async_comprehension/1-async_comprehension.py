#!/usr/bin/env python3

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This coroutine function  collects 10 random numbers
    using an async comprehensing over 'async_generator'
    and returns the 10 random numbers
    """
    result = [i async for i in async_generator()]

    return result
