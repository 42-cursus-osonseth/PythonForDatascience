def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x**2


def pow(x: int | float) -> int | float:
    """Return x raised to the power of itself."""
    return x**x


def outer(x: int | float, function) -> object:
    """Return a callable object that applies the given
       function to x and updates its value each call."""
    if not isinstance(x, (int, float)):
        raise ValueError("First arg must be in or float")
    if not callable(function):
        raise ValueError("Second arg must be a function")
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count

    return inner
