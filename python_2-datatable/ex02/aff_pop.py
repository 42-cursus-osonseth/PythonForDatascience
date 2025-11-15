from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def convert_value(value: str) -> int:
    """
    Convert a population string with suffix 'M'
    (millions) or 'k' (thousands) to an integer.
    """
    n = float(value[:-1])
    if value[-1] == "M":
        return n * 1e6
    elif value[-1] == "k":
        return n * 1e3
    else:
        return n


def main():
    """
    Load the population dataset, filter for France
    and South Korea, select columns from 1800 to 2050,
    convert population strings to numeric values, transpose
    the DataFrame, and plot population over time.

    The Y-axis is formatted in millions with an 'M' suffix,
    and the X-axis shows the years.

    Exceptions
    ----------
    Catches any exception during loading, conversion,
    or plotting and prints the error.
    """
    try:
        df = load("population_total.csv")
        new_df = df[(df["country"] == "France") |
                    (df["country"] == "South Korea")]
        filtered_col = ["country"] + [
            col for col in new_df.columns
            if col.isdigit() and 1800 <= int(col) <= 2050
        ]
        new_df = new_df[filtered_col]
        for row in range(len(new_df)):
            for val in range(1, len(new_df.columns)):
                new_df.iloc[row, val] = convert_value(new_df.iloc[row, val])
        new_df = new_df.set_index("country").T
        ax = new_df.plot(title="France Life expectancy Projection")
        plt.xlabel("Year")
        plt.ylabel("Population")
        formatter = FuncFormatter(lambda x, _: f"{int(x/1_000_000)}M")
        ax.yaxis.set_major_formatter(formatter)
        plt.show()
    except Exception as Error:
        print(Error)


if __name__ == "__main__":
    main()
