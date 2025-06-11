import pandas as pd
import os


def load(path: str) -> pd.core.frame.DataFrame:
    try:
        if not isinstance(path, str):
            raise AssertionError("Dataset path is not a string")
        if not path.lower().endswith(("csv")):
            raise AssertionError("Dataset format is not a 'csv'")
        if not os.path.exists(path):
            raise AssertionError("Dataset path does not exist")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None
