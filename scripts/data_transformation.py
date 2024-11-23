import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.interpolate import interp1d

def perform_fft(signal, sampling_rate, output_file="outputs/fft_analysis.png"):
    """
    Performs Fast Fourier Transform (FFT) on a signal and plots the frequency spectrum.

    Parameters:
    signal (array): The input signal.
    sampling_rate (float): Sampling rate of the signal (Hz).
    output_file (str): Path to save the FFT plot.
    """
    # Perform FFT
    N = len(signal)
    yf = fft(signal)  # FFT of the signal
    xf = fftfreq(N, 1 / sampling_rate)  # Frequency bins

    # Only plot the positive frequencies
    positive_freqs = xf[:N // 2]
    positive_amplitudes = np.abs(yf[:N // 2])

    # Plot FFT
    plt.figure(figsize=(10, 6))
    plt.plot(positive_freqs, positive_amplitudes, label="FFT Amplitude")
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.savefig(output_file)
    print(f"FFT analysis plot saved to {output_file}")
    plt.show()

def interpolate_missing_data(data, column):
    """
    Interpolates missing values in the specified column of a DataFrame.

    Parameters:
    data (pd.DataFrame): The input dataset.
    column (str): The column to interpolate.

    Returns:
    pd.DataFrame: Dataset with missing values interpolated.
    """
    print(f"\nInterpolating missing data for column: {column}")
    if data[column].isnull().any():
        # Linear interpolation
        data[column] = data[column].interpolate(method='linear')
        print("Missing data interpolated using linear method.")
    else:
        print("No missing data found in this column.")
    return data

if __name__ == "__main__":
    # Load the dataset
    file_path = "data/sample_data.csv"
    data = pd.read_csv(file_path, parse_dates=["timestamp"])

    # Perform FFT on temperature_c column
    signal = data["temperature_c"].values
    sampling_rate = 1  # Assuming data is recorded every second
    perform_fft(signal, sampling_rate)

    # Introduce missing values for testing interpolation
    data.loc[5:7, "temperature_c"] = np.nan
    print("\nDataset with missing values:")
    print(data.head(10))

    # Interpolate missing data
    interpolated_data = interpolate_missing_data(data, "temperature_c")
    print("\nDataset after interpolation:")
    print(interpolated_data.head(10))

    # Save the interpolated dataset
    interpolated_data.to_csv("outputs/interpolated_data.csv", index=False)
    print("Interpolated data saved to outputs/interpolated_data.csv")
