#!/usr/bin/env python3
"""
1-async_comprehension
"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    collect the random numbers from `async_generator` using asynchronous
    comprehension
    """
    random_nums = [i async for i in async_generator()]
    return random_nums
