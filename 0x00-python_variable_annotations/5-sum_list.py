#!/usr/bin/env python3
"""
5-sum_list
"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    calculate sum of values in `input_list`
    """
    sum: float = 0.0
    for n in input_list:
        sum += n
    return sum
