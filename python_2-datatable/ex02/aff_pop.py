from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def convert_value(value: str) -> int:
    n = float(value[:-1])
    if value[-1] == 'M':
        return n * 1e6
    elif value[-1] == 'k':
        return n * 1e3
    else:
        return n
        
def main():
    try:
        df = load("population_total.csv")
        new_df = df[(df['country'] == 'France') | (df['country'] == 'South Korea')]
        filtered_col = ['country'] + [col for col in new_df.columns if col.isdigit() and 1800 <= int(col) <= 2050]
        new_df = new_df[filtered_col]
        for row in range(len(new_df)):
            for val in range(1, len(new_df.columns)):
                new_df.iloc[row, val] = convert_value(new_df.iloc[row, val])
        new_df = new_df.set_index("country").T
        ax = new_df.plot(title='France Life expectancy Projection')
        plt.xlabel('Year')
        plt.ylabel('Population')
        formatter = FuncFormatter(lambda x, _: f'{int(x/1_000_000)}M')
        ax.yaxis.set_major_formatter(formatter)
        plt.show()
    except Exception as Error:
        print(Error)

if __name__ == "__main__":
    main()