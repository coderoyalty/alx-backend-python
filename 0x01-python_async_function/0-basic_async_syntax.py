#!/usr/bin/env python3
'''
0-basic_async_syntax
'''
import asyncio
import random


async def wait_random(max_delay=10):
    """
    asynchronous python function
    it waits for a random delay between 0 - `max_delay`
    """
    random_delay = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(random_delay)
    return random_delay
