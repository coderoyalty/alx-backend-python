#!/usr/bin/env python3
"""
9-element length
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    length of iterable
    """
    return [(i, len(i)) for i in lst]
