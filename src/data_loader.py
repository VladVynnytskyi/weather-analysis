import pandas as pd

def load_and_clear(filepath):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna()
    return df

def load_city_data(path):           

    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.dropna()
    return df
