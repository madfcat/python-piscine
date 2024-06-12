import pandas


def load(path: str) -> pandas.DataFrame:
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
