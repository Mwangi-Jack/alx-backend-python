#!/usr/bin/env python3
# countasync.py

import asyncio
import random

async def count(delay):
    await asyncio.sleep(delay)
    print("Count", delay)
    return delay

async def main():
    li = [count(random.uniform(0, 4)) for _ in range(4)]

    delays = []
    for task in asyncio.as_completed(li):
        result = await task
        delays.append(result)

    print(delays)

if __name__ == "__main__":
    asyncio.run(main())
