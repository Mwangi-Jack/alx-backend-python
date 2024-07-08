#!/usr/bin/env python3
"""Geting tasks"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function takes int an intager value 'max_delay'
    and returns an asyncio.task instance
    """
    return asyncio.Task(wait_random(max_delay))
