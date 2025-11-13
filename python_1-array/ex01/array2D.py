import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Check args, print the shape of list, slice the list, print the new shape
    and return the list sliced"""

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be int")
    if not isinstance(family, list):
        raise TypeError("family must be list")
    if not all(len(el) == len(family[0]) for el in family):
        raise ValueError("List must have the same size")

    f = np.array(family)
    print(f"My shape is : {f.shape}")
    new_family = family[start:end]
    f = np.array(new_family)
    print(f"My new shape is : {f.shape}")
    return new_family
