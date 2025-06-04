from data_loader import load_and_clear
from visualizer import plot_monthly_box, plot_yearly_avg, plot_rolling_avg, plot_anomalies
from analysis import show_yearly_stats

# Load Krakow weather data from CSV file

df = load_and_clear("data/krakow_weather.csv")


# plot and save average temperature
plot_yearly_avg(df)


# plot monthly boxplot
plot_monthly_box(df)

plot_rolling_avg(df)

#plot anomalies
plot_anomalies(df)

show_yearly_stats(df)
