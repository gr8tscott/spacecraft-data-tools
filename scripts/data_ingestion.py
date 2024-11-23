import pandas as pd
import numpy as np

def read_and_describe(file_path):
    """
    Reads a CSV file and displays basic information and statistics.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    try:
        # Load the data
        data = pd.read_csv(file_path, parse_dates=["timestamp"])
        print("\nData Overview:")
        print(data.head())
        print("\nData Info:")
        print(data.info())
        print("\nSummary Statistics:")
        print(data.describe())
        return data
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

def clean_data(data):
    """
    Cleans the dataset by handling missing values, outliers, and invalid entries.

    Parameters:
    data (pd.DataFrame): The dataset.

    Returns:
    pd.DataFrame: The cleaned dataset.
    """
    # Handling missing values
    print("\nHandling Missing Values...")
    missing_summary = data.isnull().sum()
    print(f"Missing Values:\n{missing_summary}")

    # Option 1: Fill missing numerical values with column mean
    num_cols = data.select_dtypes(include=[np.number]).columns
    data[num_cols] = data[num_cols].fillna(data[num_cols].mean())
    print("Missing values filled with column means.")

    # Option 2: Remove rows with any missing values
    # data = data.dropna()
    # print("Rows with missing values have been removed.")

    # Handling outliers using the Interquartile Range (IQR)
    print("\nDetecting and Handling Outliers...")
    for column in num_cols:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = ((data[column] < lower_bound) | (data[column] > upper_bound)).sum()
        print(f"{column}: {outliers} outliers detected.")
        # Cap outliers
        data[column] = np.clip(data[column], lower_bound, upper_bound)
    print("Outliers capped to the IQR range.")

    # Ensuring valid values for specific columns
    print("\nValidating Specific Columns...")
    if "temperature_c" in data.columns:
        invalid_temps = data[data["temperature_c"] < -273.15]
        if not invalid_temps.empty:
            print(f"Invalid temperatures detected:\n{invalid_temps}")
            data["temperature_c"] = data["temperature_c"].clip(lower=-273.15)

    print("\nData cleaning completed.")
    return data

if __name__ == "__main__":
    file_path = "data/sample_data.csv"  # Replace with your file path if needed
    data = read_and_describe(file_path)
    if data is not None:
        cleaned_data = clean_data(data)
        # Save cleaned data for further analysis
        cleaned_data.to_csv("outputs/cleaned_data.csv", index=False)
        print("Cleaned data saved to outputs/cleaned_data.csv")
