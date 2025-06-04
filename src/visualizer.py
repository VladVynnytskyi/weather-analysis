import matplotlib.pyplot as plt
import os


def plot_yearly_avg(df):
    # Build and save a line plot showing the average temperature for each year
    # Group by year and calculate average temperature
    yearly_avg = df.groupby(df["date"].dt.year)["temperature"].mean()
    os.makedirs("plots", exist_ok=True)

    # create the figure
    plt.figure(figsize=(10, 5))
    yearly_avg.plot(marker="o")

    # add title, x and y labels
    plt.title("Average Yearly Temperature in Cracow")
    plt.xlabel("Year")
    plt.ylabel("Temperature")

    # add grid and layout
    plt.grid(True)
    plt.tight_layout()

    # save plot
    plt.savefig("plots/yearly_temperature")
    plt.close


def plot_monthly_box(df):
    df["month"] = df["date"].dt.month  # add a 'month' column
    plt.figure(figsize=(10, 5))
    df.boxplot(column="temperature", by="month")
    plt.title("Monthly Temperature Distribution in Krakow")
    plt.suptitle("")  # removes auto title
    plt.xlabel("Month")
    plt.ylabel("Temperature")
    plt.tight_layout()
    plt.savefig("plots/monthly_boxplot.png")
    plt.close()


def plot_rolling_avg(df, window=30):

    #Build and save a line chart with a rolling average temperature (default: 30 days).

    df_sorted = df.sort_values('date') 

    df_sorted['rolling_avg'] = df_sorted['temperature'].rolling(window=window).mean()

    plt.figure(figsize=(12, 6))
    plt.plot(df_sorted['date'], df_sorted['temperature'], alpha=0.3, label='Daily Temperature')
    plt.plot(df_sorted['date'], df_sorted['rolling_avg'], color='red', label=f'{window}-day Rolling Avg')

    plt.title("Rolling Average Temperature (Krakow)")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("plots/rolling_avg_temp.png")
    plt.close()


def plot_anomalies(df):

#    Detect and visualize temperature anomalies (very high or very low temperatures).
#   Anomalies are defined as values beyond 2 standard deviations from the mean.


    mean = df['temperature'].mean()
    std = df['temperature'].std()

    high = mean + 2 * std
    low = mean - 2 * std
    df_sorted = df.sort_values('date')

    high_anomalies = df_sorted[df_sorted['temperature'] > high]
    low_anomalies = df_sorted[df_sorted['temperature'] < low]

    plt.figure(figsize=(12, 6))
    plt.plot(df_sorted['date'], df_sorted['temperature'], alpha=0.3, label='Daily Temperature')
    plt.scatter(high_anomalies['date'], high_anomalies['temperature'], color='red', label='High Anomalies')
    plt.scatter(low_anomalies['date'], low_anomalies['temperature'], color='blue', label='Low Anomalies')
    plt.axhline(high, color='red', linestyle='--', linewidth=1)
    plt.axhline(low, color='blue', linestyle='--', linewidth=1)

    plt.title("Temperature Anomalies in Krakow")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("plots/anomalies_temp.png")
    plt.close()