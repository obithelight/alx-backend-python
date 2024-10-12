#!/usr/bin/env python3
''' This module defines a function `sum_mixed_list` '''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' returns the sum of mxd_lst as float '''
    return sum(mxd_lst)
