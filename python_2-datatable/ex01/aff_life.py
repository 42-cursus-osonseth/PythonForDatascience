from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def main():
    try:
        df = load("life_expectancy_years.csv")
        france_row = df[df['country'] == 'France'].squeeze()
        france_row.iloc[1:].plot(title = 'France Life expentency Projection')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.show()
    except Exception as Error:
        print(Error)

if __name__ == "__main__":
    main()


    