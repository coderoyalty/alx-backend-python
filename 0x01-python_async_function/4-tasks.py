#!/usr/bin/env python3
"""
4-tasks
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(max_delay: int) -> List[float]:
    """
    similar with `wait_n` but returns tasks rather
    """
    tasks = [task_wait_random(max_delay) for _ in range]
    return [await task for task in asyncio.as_completed(tasks)]
