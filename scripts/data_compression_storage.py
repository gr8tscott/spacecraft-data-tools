import pandas as pd
import os
import zipfile

# IMPORTANT:
# In order to run this file, you may need to pip install: pyarrow, openpyxl

def compress_to_csv_gzip(data, output_file):
    """
    Compresses the DataFrame to a GZIP-compressed CSV file.

    Parameters:
    data (pd.DataFrame): The dataset to compress.
    output_file (str): Path to save the compressed file.
    """
    data.to_csv(output_file, index=False, compression="gzip")
    print(f"Data compressed and saved to {output_file}")

def compress_to_parquet(data, output_file):
    """
    Compresses the DataFrame to a Parquet file with Snappy compression.

    Parameters:
    data (pd.DataFrame): The dataset to compress.
    output_file (str): Path to save the Parquet file.
    """
    data.to_parquet(output_file, index=False, compression="snappy")
    print(f"Data compressed and saved to {output_file}")

def compress_to_zip(file_paths, output_file):
    """
    Compresses multiple files into a ZIP archive.

    Parameters:
    file_paths (list): List of file paths to include in the ZIP archive.
    output_file (str): Path to save the ZIP file.
    """
    with zipfile.ZipFile(output_file, "w") as zipf:
        for file_path in file_paths:
            zipf.write(file_path, os.path.basename(file_path))
    print(f"Files compressed into ZIP archive: {output_file}")

def export_to_format(data, output_file, format="csv"):
    """
    Exports the DataFrame to the specified format.

    Parameters:
    data (pd.DataFrame): The dataset to export.
    output_file (str): Path to save the file.
    format (str): Format to export ("csv", "json", "excel").
    """
    if format == "csv":
        data.to_csv(output_file, index=False)
    elif format == "json":
        data.to_json(output_file, orient="records", lines=True)
    elif format == "excel":
        data.to_excel(output_file, index=False)
    else:
        raise ValueError("Unsupported format. Choose from 'csv', 'json', or 'excel'.")
    print(f"Data exported to {output_file} in {format.upper()} format")

if __name__ == "__main__":
    # Load sample dataset
    file_path = "data/sample_temperature_data.csv"
    data = pd.read_csv(file_path)

    # Compression examples
    compress_to_csv_gzip(data, "outputs/compressed_data.csv.gz")
    compress_to_parquet(data, "outputs/compressed_data.parquet")

    # Exporting to different formats
    export_to_format(data, "outputs/analyzed_data.csv", format="csv")
    export_to_format(data, "outputs/analyzed_data.json", format="json")
    export_to_format(data, "outputs/analyzed_data.xlsx", format="excel")

    # ZIP multiple files
    files_to_compress = [
        "outputs/compressed_data.csv.gz",
        "outputs/compressed_data.parquet",
        "outputs/analyzed_data.csv",
    ]
    compress_to_zip(files_to_compress, "outputs/compressed_archive.zip")
