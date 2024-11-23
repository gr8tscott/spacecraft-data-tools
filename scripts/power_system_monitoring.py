import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os 

def calculate_energy_balance(data, generation_col, consumption_col):
    """
    Calculates the energy balance (generation - consumption) at each time step.

    Parameters:
    data (pd.DataFrame): The dataset.
    generation_col (str): Column name for power generation.
    consumption_col (str): Column name for power consumption.

    Returns:
    pd.Series: Energy balance over time.
    """
    data["energy_balance"] = data[generation_col] - data[consumption_col]
    return data["energy_balance"]

def detect_performance_deviations(data, column, lower_bound, upper_bound):
    """
    Detects deviations in performance based on predefined bounds.

    Parameters:
    data (pd.DataFrame): The dataset.
    column (str): Column to check for deviations.
    lower_bound (float): Lower bound for expected values.
    upper_bound (float): Upper bound for expected values.

    Returns:
    pd.DataFrame: Data points that are outside the expected range.
    """
    deviations = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    print(f"\nDetected Deviations in {column}:")
    print(deviations)
    return deviations

def plot_power_trends(data, generation_col, consumption_col, output_file="outputs/power_trends.png"):
    """
    Plots power generation and consumption trends over time.

    Parameters:
    data (pd.DataFrame): The dataset.
    generation_col (str): Column name for power generation.
    consumption_col (str): Column name for power consumption.
    output_file (str): Path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data["timestamp"], data[generation_col], label="Power Generation", color="green")
    plt.plot(data["timestamp"], data[consumption_col], label="Power Consumption", color="red")
    plt.xlabel("Time")
    plt.ylabel("Power (W)")
    plt.title("Power Generation vs Consumption")
    plt.legend()
    plt.grid()
    plt.savefig(output_file)
    print(f"Power trends plot saved to {output_file}")
    plt.show()

def plot_energy_balance(data, output_file="outputs/energy_balance.png"):
    """
    Plots the energy balance over time.

    Parameters:
    data (pd.DataFrame): The dataset.
    output_file (str): Path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data["timestamp"], data["energy_balance"], label="Energy Balance", color="blue")
    plt.axhline(0, color="black", linestyle="--", linewidth=1, label="Balance = 0")
    plt.xlabel("Time")
    plt.ylabel("Energy Balance (W)")
    plt.title("Energy Balance Over Time")
    plt.legend()
    plt.grid()
    plt.savefig(output_file)
    print(f"Energy balance plot saved to {output_file}")
    plt.show()

if __name__ == "__main__":
    # Load the dataset
    file_path = "data/sample_power_data.csv"
    data = pd.read_csv(file_path, parse_dates=["timestamp"])

    # Analyze energy balance
    calculate_energy_balance(data, generation_col="power_generation_w", consumption_col="power_consumption_w")

    # Detect performance deviations
    generation_deviations = detect_performance_deviations(data, "power_generation_w", lower_bound=100, upper_bound=200)
    consumption_deviations = detect_performance_deviations(data, "power_consumption_w", lower_bound=90, upper_bound=150)

    # Plot trends and energy balance
    plot_power_trends(data, generation_col="power_generation_w", consumption_col="power_consumption_w")
    plot_energy_balance(data)

    # Save results
    deviations_folder = "outputs/deviations"
    os.makedirs(deviations_folder, exist_ok=True)
    generation_deviations.to_csv(f"{deviations_folder}/generation_deviations.csv", index=False)
    consumption_deviations.to_csv(f"{deviations_folder}/consumption_deviations.csv", index=False)
    print(f"Deviation data saved to {deviations_folder}")
