from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def main():
    try:
        df = load("life_expectancy_years.csv")
        new_df = df[(df['country'] == 'France') | (df['country'] == 'South Korea')]
        print(new_df)
        print(new_df.columns)
        

    except Exception as Error:
        print(Error)

if __name__ == "__main__":
    main()