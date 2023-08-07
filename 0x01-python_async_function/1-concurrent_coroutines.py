#!/usr/bin/env python3
"""
1-concurrent_coroutines
"""
import asyncio
from typing import List, TypeVar
wait_random = __import__('0-basic_async_syntax').wait_random
T = TypeVar('T')


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    spawn `wait_random function `n` no. of times
    """
    i: int = 0
    tasks: List[T] = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    return [await task for task in asyncio.as_completed(tasks)]
