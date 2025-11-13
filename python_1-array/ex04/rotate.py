from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(img: np.array) -> np.array:
    """
    - Handle file-not-found or loading errors.
    - Slice the image array.
    - Convert the slice to grayscale using PIL.
    - Convert back to a NumPy array.
    """
    if np.array is None:
        raise FileNotFoundError("The image file could not be found or opened.")
    img = img[100:500, 450:850]
    img = Image.fromarray(img).convert("L")
    img = np.array(img)
    return img


def ft_rotate(img: np.array) -> np.array:
    """Transpose the image array in comprehension list"""
    rotate_img = [
        [img[row][col] for row in range(len(img))]
        for col in range(len(img[0]) - 1, -1, -1)
    ]
    return np.array(rotate_img)


def main():
    """
    Main program flow:
    - Load the image using ft_load.
    - Slice the image array using ft_zoom
    - Print the shape and content of the resulting array.
    - transpose image array using ft_rotate
    - Print the shape and content of the resulting array.
    - Display the grayscale image with matplotlib."""

    try:
        img_array = ft_load("animal.jpeg")
        img_array = ft_zoom(img_array)
        print(f"The shape of image is : {img_array.shape}")
        print(img_array)
        img_array = ft_rotate(img_array)
        print(f"New shape after Transpose: {img_array.shape}")
        print(img_array)
        plt.imshow(img_array, cmap="gray")
        plt.show()

    except Exception as Error:
        print(Error)


if __name__ == "__main__":
    main()
