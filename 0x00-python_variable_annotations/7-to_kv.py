#!/usr/bin/env python3
"""
This module provides a function to create a tuple with a string and the square of an int/float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of an int/float.

    Args:
        k (str): The string.
        v (Union[int, float]): The int or float.

    Returns:
        Tuple[str, float]: A tuple containing k and the square of v as a float.
    """
    return (k, float(v ** 2))

if __name__ == "__main__":
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
