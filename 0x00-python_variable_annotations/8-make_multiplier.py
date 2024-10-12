#!/usr/bin/env python3
''' This module defines a complex type function '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' returns a function `innerFunc` '''
    def innerFunc(num: float) -> float:
        ''' returns innerFunct * make_multiplier '''
        return (num * multiplier)
    return innerFunc
