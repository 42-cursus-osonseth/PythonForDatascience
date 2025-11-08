import sys
import string


def ask_input() -> str:
    """Ask and return the user input"""
    print("What is the text to count ?")
    str = sys.stdin.readline()
    return str


def count_chars(input: str) -> dict:
    """Count the chars and call de print_ouput func"""
    dict = {
        "upper letters": 0,
        "lower letters": 0,
        "punctuation marks": 0,
        "spaces": 0,
        "digit": 0,
    }
    for c in input:
        if c.isdigit():
            dict["digit"] += 1
        elif c.islower():
            dict["lower letters"] += 1
        elif c.isupper():
            dict["upper letters"] += 1
        elif c in string.punctuation:
            dict["punctuation marks"] += 1
        elif c.isspace():
            dict["spaces"] += 1
    return dict


def print_ouput(output: dict, input: str):
    """Print the dict passed as a parameter as output"""
    print(f"The text contains {len(input)} characters:")
    for key, value in output.items():
        print(f"{value} {key}")


def count_and_print(input: str):
    """call func to count and then the func to print"""
    dict = count_chars(input)
    print_ouput(dict, input)
    sys.exit(0)


def main():
    """Check args, ask input if needed and print the result of the count"""
    if len(sys.argv) == 1:
        input = ask_input()
        count_and_print(input)

    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
        input = sys.argv[1]
        count_and_print(input)
    except AssertionError as Error:
        print(f"AssertionError: {Error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
