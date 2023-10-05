#!/usr/bin/env python3
"""
This module provides a function to safely get a value from a dictionary.
"""

from typing import Mapping, TypeVar, Any, Union

# Define a TypeVar to represent the generic types for 'default' and the return value
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary or return a default value if the key is not found.

    Args:
        dct (Mapping): A dictionary-like object.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if it exists, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default

if __name__ == "__main__":
    annotations = safely_get_value.__annotations__
    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print("{}: {}".format(k, v))
