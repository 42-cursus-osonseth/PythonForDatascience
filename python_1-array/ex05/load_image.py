import numpy as np
from numpy import array
from PIL import Image


def ft_load(path: str) -> array:
    """Check if the arg is a string
    Load the image
    Convert image in RGB if it's not
    Convert image in array
    Print the shape and return the array"""
    try:
        if not isinstance(path, str):
            raise AssertionError("Assertion Error: arg must be string")
        img = Image.open(path)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img_array = np.array(img)
        return img_array

    except AssertionError as Error:
        print(Error)

    except Exception as Error:
        print(Error)
