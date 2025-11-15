import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a Pandas DataFrame and print its dimensions.

    Raises
    ------
    TypeError
        If the provided path is not a string.
    """
    if not isinstance(path, str):
        raise TypeError("arg must be a string")

    df = pd.read_csv(path)
    print(f"Loading dataset of dimensions {df.shape}")
    return df
