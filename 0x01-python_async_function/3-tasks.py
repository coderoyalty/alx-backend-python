#!/usr/bin/env python3
"""
3-tasks
"""
import asyncio
from typing import TypeVar
T = TypeVar('T')
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> T:
    """
    create a wait task for function `wait_random`
    """
    return asyncio.create_task(wait_random)
