def get_mean(args: tuple) -> int:
    """Compute the mean of the values."""
    return sum(args) / len(args)


def get_variance(args: tuple) -> float:
    """Compute the variance of the values."""
    mean = get_mean(args)
    total_variance = 0
    for val in args:
        total_variance += (val - mean) ** 2
    return total_variance / len(args)


def print_mean(args: tuple) -> None:
    """Print the mean."""
    print(f"mean : {sum(args) / len(args)}")


def continue_loop(args: tuple) -> None:
    """Do nothing for unknown option."""
    return


def print_median(args: tuple) -> None:
    """Print the median"""
    lenght = len(args)
    args = sorted(args)
    if lenght % 2 == 0:
        print(f"median : {(args[lenght // 2] + args[(lenght // 2) - 1 ]) / 2}")
    else:
        print(f"median : {args[lenght // 2 ]}")


def print_quartile(args: tuple) -> None:
    """Print Q1 and Q3"""
    args = sorted(args)
    index25 = len(args) // 4
    index75 = index25 * 3
    print(f"quartile : [{float(args[index25])}, {float(args[index75])}]")


def print_variance(args: tuple) -> None:
    """Print variance"""
    mean = get_mean(args)
    total_variance = 0
    for val in args:
        total_variance += (val - mean) ** 2
    print(f"var : {total_variance / len(args)}")


def print_standard_deviation(args: tuple) -> None:
    """Print standard deviation"""
    variance = get_variance(args)
    std_dev = variance**0.5
    print(f"std : {std_dev}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Run the selected statistical operations."""
    if not all(isinstance(el, (int, float)) for el in args):
        raise ValueError("vector arg must me int or float")
    funcs = {
        "mean": print_mean,
        "median": print_median,
        "quartile": print_quartile,
        "std": print_standard_deviation,
        "var": print_variance,
    }

    for v in kwargs.values():
        if not args:
            print("ERROR")
        else:
            f = funcs.get(v, continue_loop)
            f(args)
