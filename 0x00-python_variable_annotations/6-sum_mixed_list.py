#!/usr/bin/env python3
"""
6-sum_mixed_list
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    sum of mixed int and float values in `mxd_list`
    """
    sum: float = 0.0
    for n in mxd_lst:
        sum += float(n)
    return sum
