import string
import sys


def get_list_comprehension(s: str, n: int) -> list:
    """Return a news list with the words s > n"""
    word_len_greater_than_n = lambda x: len(x) > n
    list_comprehension = [word for word in s.split() if word_len_greater_than_n(word)]
    return list_comprehension


def ispunctuation(s: str) -> bool:
    """Checks if the string argument contains punctuation chars, returns true if it does, otherwise false"""
    for c in s:
        if c in string.punctuation:
            return True
    return False


def main():
    """check args, call get_list_comprehension and print the new list"""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        str = sys.argv[1]
        nbr = int(sys.argv[2])
        if not str.isprintable() or ispunctuation(str):
            raise AssertionError(f"punctuation or not printable char in : {str}")
        list = get_list_comprehension(str, nbr)
        print(list)
        sys.exit(0)
    except AssertionError as Error:
        print(f"AssertionError: {Error}")
        sys.exit(1)
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)


if __name__ == "__main__":
    main()
