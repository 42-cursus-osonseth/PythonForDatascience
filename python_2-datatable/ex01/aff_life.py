from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load the life expectancy dataset, select the row for France,
    and plot its life expectancy projection over the years.

    The function squeezes the DataFrame row into a Series for France,
    plots all years except the 'country' column, and labels the axes.

    Exceptions
    ----------
    Catches any exception during loading or plotting and prints the error.
    """
    try:
        df = load("life_expectancy_years.csv")
        france_row = df[df["country"] == "France"].squeeze()
        france_row.iloc[1:].plot(title="France Life expentency Projection")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
    except Exception as Error:
        print(Error)


if __name__ == "__main__":
    main()
