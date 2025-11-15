from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def format_func(value, tick_number):
    """
    Format the X-axis tick labels for a logarithmic scale.
    Values below 1000 are displayed normally.
    Values equal to or above 1000 are displayed in thousands (K).
    """
    if tick_number == 1:
        return f"{int(value)}"
    elif value < 1000:
        return f"{int(value)}"
    else:
        return f"{int(value/1000)}K"


def main():
    """
    Load the 1900 GDP and life expectancy datasets, merge them by country,
    and display a scatter plot of life expectancy versus GDP.

    The plot uses a logarithmic scale for
    the X-axis (GDP) and formats the ticks
    to show values below 1000 normally and
    values in thousands with a 'K' suffix.
    """
    try:
        income_df = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
            )
        life_df = load("life_expectancy_years.csv")
        income_1900 = income_df[["country", "1900"]]
        life_1900 = life_df[["country", "1900"]]
        merged = income_1900.merge(
            life_1900, on="country", suffixes=("_gdp", "_life")
            )
        plt.scatter(merged["1900_gdp"], merged["1900_life"])
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")

        plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(format_func))
        plt.show()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
