def callLimit(limit: int):
    """Creates a decorator that limits
      the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """Wraps the target function and enforces the call limit."""

        def limit_function(*args: any, **kwds: any):
            """Calls the original function if under the limit,
            otherwise prints an error."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function}> call too many times")
                return
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter
