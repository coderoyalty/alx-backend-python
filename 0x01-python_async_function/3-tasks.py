#!/usr/bin/env python3
"""
3-tasks
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    create a wait task for function `wait_random`
    """
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task
