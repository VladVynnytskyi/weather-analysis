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
