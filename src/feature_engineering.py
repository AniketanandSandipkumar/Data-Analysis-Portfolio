import pandas as pd

def add_time_features(df, date_col):

    df[date_col] = pd.to_datetime(df[date_col], errors='coerce', utc=True)
    df[date_col] = df[date_col].dt.tz_localize(None)
    df = df.dropna(subset=[date_col])

    df['Day'] = df[date_col].dt.day_name()
    df['Month'] = df[date_col].dt.month_name()
    df['Year'] = df[date_col].dt.year
    df['MonthNum'] = df[date_col].dt.month
    df['Weekday'] = df[date_col].dt.weekday

    return df
