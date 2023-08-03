#!/usr/bin/env python3
"""
9-element length
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    length of iterable
    """
    return [(i, len(i)) for i in lst]
