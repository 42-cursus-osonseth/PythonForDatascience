from pimp_image import ft_invert
from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_grey
from pimp_image import ft_red
from load_image import ft_load


def main():

    try:
        array = ft_load("landscape.jpg")
        if array is None:
            raise FileNotFoundError(
                "The image file could not be found or opened."
                )
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        print(ft_invert.__doc__)

    except Exception as Error:
        print(Error)


if __name__ == "__main__":
    main()
