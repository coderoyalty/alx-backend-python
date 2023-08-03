#!/usr/bin/env python3
"""
type checking
"""
import typing


def zoom_array(lst: typing.List, factor: int = 2) -> typing.List:
    """
    zoom array
    """
    zoomed_in: typing.List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
