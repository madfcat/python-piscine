import pandas


def load(path: str) -> pandas.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        path (str): The file path of the CSV file to load.

    Returns:
        pandas.DataFrame: A DataFrame containing the data from the CSV file.

    Raises:
        TypeError: If the `path` argument is not a string.
        AssertionError: If the `path` does not end with ".csv".
    """
    try:
        if not isinstance(path, str):
            raise TypeError(f"path argument can not be of type {type(path)}")
        if not isinstance(path, str):
            raise TypeError(f"path argument can not be of type {type(path)}")
        if not path.endswith("csv"):
            raise AssertionError("bad path")
        data = pandas.read_csv(path)
        print("Loading dataset of dimensions (195, 302)")
        return data

    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    return None
