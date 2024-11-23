import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_orientation(data, output_file="outputs/orientation_3d.png"):
    """
    Visualizes spacecraft orientation in 3D using roll, pitch, and yaw.

    Parameters:
    data (pd.DataFrame): The dataset containing orientation angles.
    output_file (str): Path to save the plot.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Convert degrees to radians for visualization
    roll = np.radians(data["roll_deg"])
    pitch = np.radians(data["pitch_deg"])
    yaw = np.radians(data["yaw_deg"])

    # Simulate 3D orientation vectors
    x = np.cos(yaw) * np.cos(pitch)
    y = np.sin(yaw) * np.cos(pitch)
    z = np.sin(pitch)

    # Plot the 3D trajectory
    ax.quiver(0, 0, 0, x, y, z, length=1, normalize=True)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("3D Spacecraft Orientation")
    plt.savefig(output_file)
    print(f"3D orientation plot saved to {output_file}")
    plt.show()

if __name__ == "__main__":
    file_path = "data/orientation_sample.csv"
    data = pd.read_csv(file_path, parse_dates=["timestamp"])
    plot_3d_orientation(data)
