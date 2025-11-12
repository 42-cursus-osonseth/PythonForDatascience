import numpy as np


def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Check the args and raise exception if they are not good.
    Calculate the Body Mass Index (BMI) for each pair of height and weight.

    - Converts height and weight lists to np.array for vectorized operations.
    - Computes BMI using w / (h**2) directly on arrays.
    - Converts the resulting np.array back to a Python list.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Height and weight must be lists")
    if len(height) != len(weight):
        raise ValueError("Height and weight must have the same length")
    if not all(isinstance(el, (int, float)) for el in height):
        raise TypeError("All elements of height must be int or float")
    if not all(isinstance(el, (int, float)) for el in weight):
        raise TypeError("All elements of weight must be int or float")
    if not all(el > 0 for el in height):
        raise ValueError(
            "All heights must be positive (division by zero impossible)")
    h = np.array(height)
    w = np.array(weight)
    return list(w / (h**2))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check the args and raise exception if they are not good.
    Check for each BMI whether it exceeds a given limit.

    - Converts the input list to np.array.
    - Compares the array to the scalar limit in a vectorized way.
    - Converts the result back to a Python list.
    """
    if not isinstance(bmi, list) or not isinstance(limit, int):
        raise TypeError("Bmi must be list and limit an int")
    if not all(isinstance(el, (int, float)) for el in bmi):
        raise ValueError("All elements of bmi must be int or float")

    bmi_arr = np.array(bmi)
    return list(bmi_arr > limit)
