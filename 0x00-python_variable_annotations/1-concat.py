#!/usr/bin/env python3
"""
This module provides a function to concatenate two strings.
"""
def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenation of str1 and str2.
    """
    return str1 + str2

if __name__ == "__main__":
    str1 = "egg"
    str2 = "shell"
    print(concat(str1, str2) == "{}{}".format(str1, str2))
