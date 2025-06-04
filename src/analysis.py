import pandas as pd


def get_yearly_avg(df):
    """Return average temperature grouped by year"""
    return df.groupby(df['date'].dt.year)['temperature'].mean()

def get_max_anomaly_city(df):
    """Return max temperature and its date"""
    max_temp = df['temperature'].max()
    date = df[df['temperature'] == max_temp]['date'].values[0]
    return max_temp, pd.to_datetime(date).date()


def get_min_anomaly_city(df):
    """Return min temperature and its date"""
    min_temp = df['temperature'].min()
    date = df[df['temperature'] == min_temp]['date'].values[0]
    return min_temp, pd.to_datetime(date).date()

def show_yearly_stats(df):
    #Display yearly average temperatures, and the dates of max/min temperatures.

    yearly_avg = df.groupby(df['date'].dt.year)['temperature'].mean().round(2)
    print("Average temperature by year:")
    print(yearly_avg)

    max_temp = df['temperature'].max()
    max_date = df[df['temperature'] == max_temp]['date'].iloc[0]
    print(f"\n Highest temperature: {max_temp}°C on {max_date.date()}")

    min_temp = df['temperature'].min()
    min_date = df[df['temperature'] == min_temp]['date'].iloc[0]
    print(f" Lowest temperature: {min_temp}°C on {min_date.date()}")

def show_city_stats(df, city_name="City"):
    
    #Show yearly average temperature and extreme anomalies for a given city.

    yearly = get_yearly_avg(df)
    print(f"\n Average yearly temperature in {city_name}:")
    print(yearly.round(2))

    max_temp, max_date = get_max_anomaly_city(df)
    min_temp, min_date = get_min_anomaly_city(df)

    print(f"\n {city_name} - Highest temperature: {max_temp}°C on {max_date}")
    print(f" {city_name} - Lowest temperature: {min_temp}°C on {min_date}")
