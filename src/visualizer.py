import matplotlib.pyplot as plt
import os

def plot_yearly_avg(df):
    #Build and save a line plot showing the average temperature for each year
    # Group by year and calculate average temperature
    yearly_avg = df.groupby(df['date'].dt.year)['temperature'].mean()
    os.makedirs("plots", exist_ok=True)

    #Create the figure
    plt.figure(figsize=(10,5))
    yearly_avg.plot(marker='o')

    #add title and exis labels
    plt.title("Average Yearly Temperature in Cracow")
    plt.xlabel("Year")
    plt.ylabel("Temperature")

    #add grid and layout
    plt.grid(True)
    plt.tight_layout()

    #Save plot
    plt.savefig("plots/yearly_temperature")
    plt.close
