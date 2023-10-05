#!/usr/bin/env python3
"""
This module provides a function to calculate the floor of a float.
"""

import math

def floor(n: float) -> int:
    """
    Calculate the floor of a float and return the result as an integer.

    Args:
        n (float): The input float.

    Returns:
        int: The floor of the input float.
    """
    return math.floor(n)

if __name__ == "__main__":
    ans = floor(3.14)
    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
