import os
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Create the anomalies folder if it doesn't exist
os.makedirs("outputs/anomalies", exist_ok=True)

def threshold_based_detection(data, column, threshold, output_file="outputs/anomalies/threshold_anomalies.csv"):
    """
    Detects anomalies based on a predefined threshold.

    Parameters:
    data (pd.DataFrame): The dataset.
    column (str): The column to check for anomalies.
    threshold (float): The threshold value.
    output_file (str): Path to save the anomalies.

    Returns:
    pd.DataFrame: DataFrame with anomalies.
    """
    anomalies = data[data[column] > threshold]
    print(f"\nThreshold-Based Anomalies (>{threshold}) in {column}:")
    print(anomalies)

    anomalies.to_csv(output_file, index=False)
    print(f"Threshold-based anomalies saved to {output_file}")
    return anomalies

def z_score_detection(data, column, threshold=3.0, output_file="outputs/anomalies/z_score_anomalies.csv"):
    """
    Detects anomalies using Z-scores.

    Parameters:
    data (pd.DataFrame): The dataset.
    column (str): The column to check for anomalies.
    threshold (float): Z-score threshold for anomalies.
    output_file (str): Path to save the anomalies.

    Returns:
    pd.DataFrame: Dataset with Z-scores and anomaly flags.
    """
    mean = data[column].mean()
    std = data[column].std()
    data["z_score"] = (data[column] - mean) / std
    data["z_anomaly"] = (data["z_score"].abs() > threshold).astype(int)

    anomalies = data[data["z_anomaly"] == 1]
    print(f"\nZ-Score-Based Anomalies in {column}:")
    print(anomalies)

    anomalies.to_csv(output_file, index=False)
    print(f"Z-Score anomalies saved to {output_file}")
    return data

def isolation_forest_detection(data, column, contamination=0.05, output_file="outputs/anomalies/isolation_forest_anomalies.csv"):
    """
    Detects anomalies using Isolation Forest.

    Parameters:
    data (pd.DataFrame): The dataset.
    column (str): The column to check for anomalies.
    contamination (float): The proportion of anomalies in the dataset.
    output_file (str): Path to save the anomalies.

    Returns:
    pd.DataFrame: Dataset with anomaly flags.
    """
    isolation_forest = IsolationForest(contamination=contamination, random_state=42)
    data["if_anomaly"] = isolation_forest.fit_predict(data[[column]])
    data["if_anomaly"] = (data["if_anomaly"] == -1).astype(int)

    anomalies = data[data["if_anomaly"] == 1]
    print(f"\nIsolation Forest Anomalies in {column}:")
    print(anomalies)

    anomalies.to_csv(output_file, index=False)
    print(f"Isolation Forest anomalies saved to {output_file}")
    return data

if __name__ == "__main__":
    # Load the dataset
    file_path = "outputs/interpolated_data.csv"
    data = pd.read_csv(file_path, parse_dates=["timestamp"])

    # Threshold-Based Detection
    threshold_anomalies = threshold_based_detection(data, "temperature_c", threshold=23.0)

    # Z-Score-Based Detection
    z_score_data = z_score_detection(data, "temperature_c", threshold=2.5)

    # Isolation Forest Detection
    isolation_forest_data = isolation_forest_detection(data, "temperature_c", contamination=0.1)

    # Save updated datasets
    z_score_data.to_csv("outputs/anomalies/z_score_data.csv", index=False)
    isolation_forest_data.to_csv("outputs/anomalies/isolation_forest_data.csv", index=False)
    print("\nAnomaly detection completed. Results saved to outputs/anomalies/")
