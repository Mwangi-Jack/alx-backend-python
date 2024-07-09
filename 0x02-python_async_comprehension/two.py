#!/usr/bin/env python3

import asyncio
from typing import Generator

async def numbers(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i
        # await asyncio.sleep(0.5)

async def funcAsync():
    result = [i async for i in numbers(10) if i % 2]
    print(result)
    return result



if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    print(event_loop)
    try:
        event_loop.run_until_complete(funcAsync())
    finally:
        event_loop.close()
