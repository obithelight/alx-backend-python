#!/usr/bin/env python3
''' A Python3 Module '''
from typing import Mapping, TypeVar, Any, Union


K = TypeVar("K")  # Key Type (Can be Any)
V = TypeVar("V")  # Value Type (Maintains consistency)

def safely_get_value(dct: Mapping[K, V], key: K, default: Union[V, None] = None) -> Union[V, None]:
    if key in dct:
        return dct[key]
    else:
        return default
