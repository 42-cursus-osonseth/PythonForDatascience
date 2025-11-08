import sys

argv = sys.argv
if len(argv) < 2:
    sys.exit(1)
try:
    assert len(argv) == 2, "more than one argument is provided"
    nbr = int(argv[1])
    str = "I'm Even." if nbr % 2 == 0 else "I'm Odd."
    print(str)
except AssertionError as error:
    print(f"AssertionError: {error}")
    sys.exit(1)
except ValueError:
    print("AssertionError: Argument is not an integer")
    sys.exit(1)
