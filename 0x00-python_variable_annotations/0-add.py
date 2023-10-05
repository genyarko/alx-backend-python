#!/usr/bin/env python3
"""
This module provides a function to add two floating-point numbers.
"""

def add(a: float, b: float) -> float:
    """
    Add two floating-point numbers and return the result.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    print(add(1.11, 2.22) == 1.11 + 2.22)
