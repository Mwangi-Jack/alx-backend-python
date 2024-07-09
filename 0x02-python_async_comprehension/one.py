#!/usr/bin/python3

from typing import Generator

def generate(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i


for i in generate(5):
    print(i)
