from load_csv import load

try:
    print(load("life_expectancy_years.csv"))
except Exception as Error:
    print(Error)
