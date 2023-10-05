#!/usr/bin/env python3
"""
This module provides a function to convert a float to its string representation.
"""

def to_str(n: float) -> str:
    """
    Convert a float to its string representation and return the result.

    Args:
        n (float): The input float.

    Returns:
        str: The string representation of the input float.
    """
    return str(n)

if __name__ == "__main__":
    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
