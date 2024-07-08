#!/usr/bin/python3
"""Measuring runtime"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function takes in two intagers 'n' and
    'max_delay' and measures the run time of a function
    and returns the time in float
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    t = time.perf_counter()
    total_time = t - s

    return total_time / n
