from numpy import array
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> array:
    """
    Inverts the colors of the input RGB image.
    Each channel value is replaced by 255 minus its current value.
    """
    if not isinstance(array, np.ndarray):
        raise AssertionError("Assertion Error: Arg must be np.ndarray")
    cpy = array.copy()
    cpy[:, :, 0] = 255 - cpy[:, :, 0]
    cpy[:, :, 1] = 255 - cpy[:, :, 1]
    cpy[:, :, 2] = 255 - cpy[:, :, 2]
    plt.imshow(cpy)
    plt.show()
    return cpy


def ft_red(array) -> array:
    """
    Applies a red filter to the input RGB image.
    Keeps only the red channel; green and blue channels are set to 0.
    """
    if not isinstance(array, np.ndarray):
        raise AssertionError("Assertion Error: Arg must be np.ndarray")
    cpy = array.copy()
    cpy[:, :, 1] = 0
    cpy[:, :, 2] = 0
    plt.imshow(cpy)
    plt.show()
    return cpy


def ft_green(array) -> array:
    """
    Applies a green filter to the input RGB image.
    Keeps only the green channel; red and blue channels are set to 0.
    """
    if not isinstance(array, np.ndarray):
        raise AssertionError("Assertion Error: Arg must be np.ndarray")
    cpy = array.copy()
    cpy[:, :, 0] = 0
    cpy[:, :, 2] = 0
    plt.imshow(cpy)
    plt.show()
    return cpy


def ft_blue(array) -> array:
    """
    Applies a blue filter to the input RGB image.
    Keeps only the blue channel; red and green channels are set to 0.
    """
    if not isinstance(array, np.ndarray):
        raise AssertionError("Assertion Error: Arg must be np.ndarray")
    cpy = array.copy()
    cpy[:, :, 0] = 0
    cpy[:, :, 1] = 0
    plt.imshow(cpy)
    plt.show()
    return cpy


def ft_grey(array) -> array:
    """
    Converts the input RGB image to grayscale.
    Uses the green channel to set all three channels,
    producing a monochrome image.
    """
    if not isinstance(array, np.ndarray):
        raise AssertionError("Assertion Error: Arg must be np.ndarray")
    copy = array.copy()
    grey_channel = copy[:, :, 1]
    copy[:, :, 0] = grey_channel
    copy[:, :, 1] = grey_channel
    copy[:, :, 2] = grey_channel
    plt.imshow(copy)
    plt.show()
    return copy


def main():
    print("coucou")


if __name__ == "__main__":
    main()
