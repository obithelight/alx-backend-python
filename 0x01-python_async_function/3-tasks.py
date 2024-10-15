#!/usr/bin/env python3
"""This module defines the function `task_wait_random`"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an integer max_delay and returns a `asyncio.Task`"""
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
