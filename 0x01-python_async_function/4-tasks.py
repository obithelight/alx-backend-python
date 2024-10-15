#!/usr/bin/env python3
''' A Python3 Module '''

import asyncio
from typing import List


task_wait_random = __import__('1-concurrent_coroutines').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    alters `wait_n` code into a new function called `task_wait_n`
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
