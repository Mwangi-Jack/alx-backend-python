#!/usr/bin/env python3

# rand.py

import asyncio
import random

# ANSI colors

c = (
	"\033[0m",
	"\033[36m",
	"\033[91m",
	"\033[35m"
)

async def makerandom(idx: int, threshold: int = 6) -> int:
    """
    this function takes in two keywords of type int i.e idx
     and threshold
    """
    print(c[idx + 1] + f"Initialized makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"makerandom({idx}) == {i} too low; retrying")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return i

async def main():
    """main function"""
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")