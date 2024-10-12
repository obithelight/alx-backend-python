#!/usr/bin/env python3
''' This module defines a function to_kv '''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    ''' complex type function that returns a tuple '''
    return (k, v ** 2)
