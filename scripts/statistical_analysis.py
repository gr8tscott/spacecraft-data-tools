import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def calculate_descriptive_statistics(data):
    """
    Calculates and prints descriptive statistics for numerical columns.
    Prints: the count, mean, standard deviation, minimum, maximum, and percentiles for each numerical column
    
    Parameters:
    data (pd.DataFrame): The dataset.

    Returns:
    pd.DataFrame: DataFrame containing descriptive statistics.
    """
    print("\nDescriptive Statistics:")
    stats = data.describe().T
    print(stats)
    return stats

def plot_correlation_matrix(data, output_file="outputs/correlation_matrix.png"):
    """
    Generates a correlation matrix heatmap for numerical variables.

    Parameters:
    data (pd.DataFrame): The dataset.
    output_file (str): Path to save the heatmap.
    """
    print("\nGenerating Correlation Matrix...")
    corr_matrix = data.corr()
    print(corr_matrix)

    # Plot the correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.savefig(output_file)
    print(f"Correlation matrix heatmap saved to {output_file}")
    plt.show()

if __name__ == "__main__":
    # Load the cleaned dataset
    file_path = "outputs/cleaned_data.csv"  # Replace with your cleaned dataset file
    data = pd.read_csv(file_path, parse_dates=["timestamp"])

    # Drop non-numerical columns for analysis
    numeric_data = data.select_dtypes(include=[np.number])

    # Descriptive Statistics
    stats = calculate_descriptive_statistics(numeric_data)

    # Correlation Matrix
    plot_correlation_matrix(numeric_data)
