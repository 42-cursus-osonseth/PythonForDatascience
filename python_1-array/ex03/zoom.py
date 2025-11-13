import numpy as np
from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt


def main():
    """
    Main program flow:
    - Load the image using ft_load.
    - Handle file-not-found or loading errors.
    - Slice the image array.
    - Convert the slice to grayscale using PIL.
    - Convert back to a NumPy array.
    - Print the shape and content of the resulting array.
    - Display the grayscale image with matplotlib.
    """


try:
    img_to_array = ft_load("animal.jpeg")
    if img_to_array is None:
        raise FileNotFoundError("The image file could not be found or opened.")
    print(img_to_array)
    img_to_array = img_to_array[100:500, 450:850]
    img = Image.fromarray(img_to_array).convert("L")
    img_to_array = np.array(img)
    plt.imshow(img_to_array, cmap="gray")
    print(f"New shape after slicing: {img_to_array.shape}")
    print(img_to_array)
    plt.show()


except Exception as Error:
    print(Error)
    exit(1)


if __name__ == "__main__":
    main()
