import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_time_series(data, columns, output_file="outputs/time_series_plot.png"):
    """
    Plots time-series data for specified columns using Matplotlib and Seaborn.

    Parameters:
    data (pd.DataFrame): The dataset.
    columns (list): List of column names to plot.
    output_file (str): Path to save the plot.
    """
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    for column in columns:
        plt.plot(data["timestamp"], data[column], label=column)
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.title("Time-Series Data")
    plt.legend()
    plt.grid(True)
    plt.savefig(output_file)
    print(f"Static time-series plot saved to {output_file}")
    plt.show()

def plot_time_series_interactive(data, columns):
    """
    Creates an interactive time-series plot using Plotly.

    Parameters:
    data (pd.DataFrame): The dataset.
    columns (list): List of column names to plot.
    """
    fig = px.line(data, x="timestamp", y=columns, title="Interactive Time-Series Data")
    fig.update_layout(xaxis_title="Time", yaxis_title="Values")
    fig.show()

if __name__ == "__main__":
    file_path = "data/sample_data.csv"
    data = pd.read_csv(file_path, parse_dates=["timestamp"])
    plot_time_series(data, ["temperature_c", "voltage_v"])
    plot_time_series_interactive(data, ["temperature_c", "voltage_v"])
