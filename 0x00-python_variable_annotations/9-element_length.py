#!/usr/bin/env python3
''' This module defines a function annotation '''
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' returns an iterable object '''
    return [(i, len(i)) for i in lst]
