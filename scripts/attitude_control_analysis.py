import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def quaternion_to_rotation_matrix(q):
    """
    Converts a quaternion to a rotation matrix.

    Parameters:
    q (array): Quaternion [q0, q1, q2, q3].

    Returns:
    np.array: 3x3 rotation matrix.
    """
    q0, q1, q2, q3 = q
    return np.array([
        [1 - 2 * (q2**2 + q3**2), 2 * (q1 * q2 - q0 * q3), 2 * (q1 * q3 + q0 * q2)],
        [2 * (q1 * q2 + q0 * q3), 1 - 2 * (q1**2 + q3**2), 2 * (q2 * q3 - q0 * q1)],
        [2 * (q1 * q3 - q0 * q2), 2 * (q2 * q3 + q0 * q1), 1 - 2 * (q1**2 + q2**2)]
    ])

def quaternion_to_euler_angles(q):
    """
    Converts a quaternion to Euler angles (roll, pitch, yaw).

    Parameters:
    q (array): Quaternion [q0, q1, q2, q3].

    Returns:
    tuple: Euler angles (roll, pitch, yaw) in degrees.
    """
    q0, q1, q2, q3 = q

    # Roll (x-axis rotation)
    roll = np.degrees(np.arctan2(2 * (q0 * q1 + q2 * q3), 1 - 2 * (q1**2 + q2**2)))

    # Pitch (y-axis rotation)
    pitch = np.degrees(np.arcsin(2 * (q0 * q2 - q3 * q1)))

    # Yaw (z-axis rotation)
    yaw = np.degrees(np.arctan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2**2 + q3**2)))

    return roll, pitch, yaw

def validate_quaternion(q):
    """
    Validates a quaternion by checking its normalization.

    Parameters:
    q (array): Quaternion [q0, q1, q2, q3].

    Returns:
    bool: True if normalized, False otherwise.
    """
    norm = np.linalg.norm(q)
    return np.isclose(norm, 1.0)

def compare_sensor_data(gyro_data, star_tracker_data):
    """
    Compares gyroscope data with star tracker data to identify discrepancies.

    Parameters:
    gyro_data (pd.DataFrame): Angular velocity data from gyroscope.
    star_tracker_data (pd.DataFrame): Orientation data from star tracker.

    Returns:
    pd.DataFrame: Differences between gyroscope and star tracker orientations.
    """
    differences = star_tracker_data - gyro_data
    return differences

def plot_orientation(data, title, output_file):
    """
    Plots orientation data (roll, pitch, yaw) over time.

    Parameters:
    data (pd.DataFrame): Orientation data with columns ['timestamp', 'roll', 'pitch', 'yaw'].
    title (str): Title of the plot.
    output_file (str): Path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data["timestamp"], data["roll"], label="Roll")
    plt.plot(data["timestamp"], data["pitch"], label="Pitch")
    plt.plot(data["timestamp"], data["yaw"], label="Yaw")
    plt.xlabel("Time")
    plt.ylabel("Angle (degrees)")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.savefig(output_file)
    print(f"Orientation plot saved to {output_file}")
    plt.show()

if __name__ == "__main__":
    # Load sample attitude data
    file_path = "data/sample_attitude_data.csv"
    data = pd.read_csv(file_path, parse_dates=["timestamp"])

    # Quaternion validation
    data["quaternion_valid"] = data[["q0", "q1", "q2", "q3"]].apply(lambda q: validate_quaternion(q.values), axis=1)
    print(f"Quaternion Validation Results:\n{data[['timestamp', 'quaternion_valid']]}")

    # Convert quaternion to Euler angles
    data[["roll", "pitch", "yaw"]] = data[["q0", "q1", "q2", "q3"]].apply(lambda q: pd.Series(quaternion_to_euler_angles(q.values)), axis=1)

    # Plot orientation data
    plot_orientation(data, "Spacecraft Orientation Over Time", "outputs/orientation_plot.png")

    # Compare gyroscope and star tracker data
    gyro_data = pd.read_csv("data/sample_gyro_data.csv", parse_dates=["timestamp"])
    star_tracker_data = data[["timestamp", "roll", "pitch", "yaw"]]
    differences = compare_sensor_data(gyro_data[["roll", "pitch", "yaw"]], star_tracker_data[["roll", "pitch", "yaw"]])
    print(f"\nDifferences between Gyroscope and Star Tracker Data:\n{differences}")
