import pandas as pd

def get_stats(file, separator):
    df = pd.read_csv(file, sep=separator)
    return df.describe()