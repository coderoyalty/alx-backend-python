#!/usr/bin/env python3
"""
0-async_generator
"""
import asyncio
import typing
import random


async def async_generator() -> typing.Generator[float, None, None]:
    """
    asynchronously wait a second then yield a random number
    from 0-10 while looping 10 times.
    """
    for _ in range(0, 10):
        await asyncio.sleep(1.0)
        yield random.uniform(0, 10)
