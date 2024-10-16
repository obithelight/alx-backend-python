#!/usr/bin/env python3
''' A Coroutine Async Generator '''

import asyncio
import random
from typing import Generator


async def async_generator() -> AsyncGenerator[float, None]:
    '''
    Loops 10 times asynchronously and yields a random number between 0 and 10
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
