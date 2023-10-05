#!/usr/bin/env python3
"""
This module provides a function to safely get the first element of a list.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely get the first element of a list, or return None if the list is empty.

    Args:
        lst (Sequence[Any]): A sequence (list or other iterable) containing elements of any type.

    Returns:
        Union[Any, None]: The first element of the sequence, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

if __name__ == "__main__":
    print(safe_first_element.__annotations__)
