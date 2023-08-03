#!/usr/bin/env python3
"""
8-make_multiplier
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    make a function that returns `multiplier * n`  
    """
    def func(n: float) -> float:
        return (n * multiplier)
    return func
