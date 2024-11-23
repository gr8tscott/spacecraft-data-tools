import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def track_temperature_changes(data, column, output_file="outputs/temperature_trends.png"):
    """
    Plots temperature changes over time.

    Parameters:
    data (pd.DataFrame): Dataset with temperature data.
    column (str): Column name for temperature.
    output_file (str): Path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data["timestamp"], data[column], label="Temperature")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Changes Over Time")
    plt.grid()
    plt.legend()
    plt.savefig(output_file)
    print(f"Temperature trends plot saved to {output_file}")
    plt.show()

def detect_temperature_anomalies(data, column, threshold, output_file="outputs/temperature_anomalies.csv"):
    """
    Detects temperature anomalies based on a threshold.

    Parameters:
    data (pd.DataFrame): Dataset with temperature data.
    column (str): Column name for temperature.
    threshold (float): Temperature threshold for anomalies.
    output_file (str): Path to save anomalies.

    Returns:
    pd.DataFrame: DataFrame with anomalies.
    """
    anomalies = data[data[column] > threshold]
    print(f"\nDetected Temperature Anomalies (>{threshold}°C):")
    print(anomalies)

    anomalies.to_csv(output_file, index=False)
    print(f"Temperature anomalies saved to {output_file}")
    return anomalies

def heat_dissipation_model(t, T0, tau, Tamb):
    """
    Exponential decay model for heat dissipation.

    Parameters:
    t (float): Time (s).
    T0 (float): Initial temperature.
    tau (float): Time constant.
    Tamb (float): Ambient temperature.

    Returns:
    float: Predicted temperature at time t.
    """
    return T0 * np.exp(-t / tau) + Tamb

def fit_heat_dissipation(data, time_column, temp_column, output_file="outputs/heat_dissipation_fit.png"):
    """
    Fits an exponential decay model to heat dissipation data.

    Parameters:
    data (pd.DataFrame): Dataset with time and temperature data.
    time_column (str): Column name for time.
    temp_column (str): Column name for temperature.
    output_file (str): Path to save the fit plot.
    """
    time = data[time_column].values
    temperature = data[temp_column].values

    # Fit the heat dissipation model
    popt, _ = curve_fit(heat_dissipation_model, time, temperature, p0=[temperature[0], 100, 20])
    T0, tau, Tamb = popt
    print(f"\nFitted Heat Dissipation Parameters:")
    print(f"Initial Temperature (T0): {T0:.2f}°C")
    print(f"Time Constant (tau): {tau:.2f}s")
    print(f"Ambient Temperature (Tamb): {Tamb:.2f}°C")

    # Plot the fit
    plt.figure(figsize=(10, 6))
    plt.scatter(time, temperature, label="Observed Data", color="red")
    plt.plot(time, heat_dissipation_model(time, *popt), label="Fitted Model", color="blue")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.title("Heat Dissipation Fit")
    plt.legend()
    plt.grid()
    plt.savefig(output_file)
    print(f"Heat dissipation fit plot saved to {output_file}")
    plt.show()

if __name__ == "__main__":
    # Load the dataset
    file_path = "data/sample_temperature_data.csv"
    data = pd.read_csv(file_path, parse_dates=["timestamp"])

    # Track temperature changes
    track_temperature_changes(data, "temperature_c")

    # Detect temperature anomalies
    anomalies = detect_temperature_anomalies(data, "temperature_c", threshold=50.0)

    # Fit heat dissipation model
    dissipation_data = data[["time_s", "temperature_c"]].dropna()
    fit_heat_dissipation(dissipation_data, "time_s", "temperature_c")
