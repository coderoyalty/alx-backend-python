#!/usr/bin/env python3
"""
100-safe_first_element
"""
import typing as tp


def safe_first_element(lst: tp.Sequence[tp.Any]) -> tp.Union[tp.Any, None]:
    """
    safe first element
    """
    if lst:
        return lst[0]
    else:
        return None
