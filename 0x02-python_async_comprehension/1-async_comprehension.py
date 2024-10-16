#!/usr/bin/env python3
''' A Coroutine Async Comprehension '''

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Collects 10 random numbers using async comprehensing and returns them
    '''
    return [_ async for _ in async_generator()]
