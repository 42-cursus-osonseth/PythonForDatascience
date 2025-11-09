import sys


def input_into_morse_str(s: str) -> str:
    """Build a string to return  from the input and the Morse dictionary"""
    MORSE_DICT = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": "/",
    }
    morse_str = " ".join(MORSE_DICT[c] for c in s)
    return morse_str


def main():
    """Check Args and call input_into_morse_str"""

    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        assert all(
            char.isalnum() or char.isspace() for char in sys.argv[1]
        ), "the arguments are bad"
        input = sys.argv[1].upper()
        morse_output = input_into_morse_str(input)
        print(morse_output)

    except AssertionError as Error:
        print(f"AssertionError: {Error}")


if __name__ == "__main__":
    main()
