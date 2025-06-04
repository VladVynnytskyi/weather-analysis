from data_loader import load_and_clear, load_city_data
from visualizer import plot_monthly_box, plot_yearly_avg, plot_rolling_avg, plot_anomalies, plot_compare_cities
from analysis import show_yearly_stats, show_city_stats

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



df_krakow = load_and_clear("data/krakow_weather.csv")
df_lviv = load_city_data("data/lviv_weather.csv")

plot_compare_cities(df_krakow, df_lviv)

show_city_stats(df_lviv, city_name="Lviv")

