from data_loader import load_and_clear
from visualizer import plot_yearly_avg, plot_monthly_box

# Load Krakow weather data from CSV file

df = load_and_clear("data/krakow_weather.csv")

#ploat and save average temparature
plot_yearly_avg(df)

# plot monthly boxplot
plot_monthly_box(df)

