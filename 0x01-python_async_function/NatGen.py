#!/usr/bin/env python3
# NatGen.py
"""
prefer native code coroutines for the sake of
being explicit rather than implicit
"""

import asyncio

def stuff():
    pass

@asyncio.coroutine
def py34_coro():
    """Generator-based coroutine, older syntax"""
    yield from stuff()

async def py35_coro():
    """Native coroutine, modern syntax"""
    await stuff()


