#!/usr/bin/env python3
"""
7-to_kv
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    return `k` and `v` as a tuple
    """
    rv: typing.Tuple[str, float] = (k, v)
    return rv
