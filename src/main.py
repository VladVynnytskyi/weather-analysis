from data_loader import load_and_clear
from visualizer import plot_monthly_box, plot_yearly_avg

# Load Krakow weather data from CSV file

df = load_and_clear("data/krakow_weather.csv")


# plot and save average temperature
plot_yearly_avg(df)


# plot monthly boxplot
plot_monthly_box(df)
