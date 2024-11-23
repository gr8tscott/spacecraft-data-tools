import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

def butter_lowpass_filter(data, cutoff, fs, order=4):
    """
    Applies a low-pass filter to the data.

    Parameters:
    data (array): The input data.
    cutoff (float): The cutoff frequency.
    fs (float): The sampling rate (Hz).
    order (int): The order of the filter.

    Returns:
    array: The filtered data.
    """
    nyquist = 0.5 * fs  # Nyquist frequency
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, data)

def butter_highpass_filter(data, cutoff, fs, order=4):
    """
    Applies a high-pass filter to the data.
    """
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return filtfilt(b, a, data)

def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    """
    Applies a band-pass filter to the data.
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band', analog=False)
    return filtfilt(b, a, data)

def plot_filtered_data(original, filtered, title, output_file):
    """
    Plots the original and filtered data for comparison.

    Parameters:
    original (array): Original data.
    filtered (array): Filtered data.
    title (str): Plot title.
    output_file (str): Path to save the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(original, label="Original Signal", alpha=0.7)
    plt.plot(filtered, label="Filtered Signal", linewidth=2)
    plt.title(title)
    plt.xlabel("Sample Index")
    plt.ylabel("Signal Value")
    plt.legend()
    plt.grid()
    plt.savefig(output_file)
    print(f"{title} plot saved to {output_file}")
    plt.show()

if __name__ == "__main__":
    # Load sample data (cleaned)
    file_path = "outputs/cleaned_data.csv"
    data = pd.read_csv(file_path)

    # Assuming we're filtering the "temperature_c" column
    signal = data["temperature_c"].values
    fs = 1  # Sampling rate (e.g., 1 Hz if data is recorded every second)
    
    # Low-pass filter
    lowpass_cutoff = 0.1  # Adjust cutoff frequency as needed
    filtered_low = butter_lowpass_filter(signal, lowpass_cutoff, fs)
    plot_filtered_data(
        signal, filtered_low, "Low-Pass Filter", "outputs/low_pass_filtered.png"
    )

    # High-pass filter
    highpass_cutoff = 0.01  # Adjust cutoff frequency as needed
    filtered_high = butter_highpass_filter(signal, highpass_cutoff, fs)
    plot_filtered_data(
        signal, filtered_high, "High-Pass Filter", "outputs/high_pass_filtered.png"
    )

    # Band-pass filter
    lowcut = 0.01
    highcut = 0.1
    filtered_band = butter_bandpass_filter(signal, lowcut, highcut, fs)
    plot_filtered_data(
        signal, filtered_band, "Band-Pass Filter", "outputs/band_pass_filtered.png"
    )
