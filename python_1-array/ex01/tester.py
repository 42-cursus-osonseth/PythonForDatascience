from array2D import slice_me


def main():

    try:
        family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))

        # Test with differentes list size
        # family = [[1.80, 78.4], [2.15, 102.7, 3], [2 , 98.5], [1.88, 75.2]]
        # print(slice_me(family, 0, 2))

        # Test with a tupple
        # family = ((1, 2), (3, 4), (5, 6))
        # print(slice_me(family, 1, -2))

    except Exception as Error:
        print(Error)


if __name__ == "__main__":
    main()
