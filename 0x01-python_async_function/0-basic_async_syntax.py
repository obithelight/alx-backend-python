#!/usr/bin/env python3
''' A Python3 Module '''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    asynchronous coroutine, takes in an integer that waits for a random delay
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
