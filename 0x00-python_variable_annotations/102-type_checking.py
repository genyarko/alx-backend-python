from typing import Tuple, List, Union

def zoom_array(lst: Tuple[Union[int, float], ...], factor: int = 2) -> Tuple[Union[int, float], ...]:
    zoomed_in: List[Union[int, float]] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)

array: Tuple[Union[int, float], ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
