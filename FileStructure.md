## **Repository Structure**

### **1. Scripts**
#### **Data Ingestion and Cleaning**
- **`data_ingestion.py`**: Reads large CSV files, handles missing values, detects outliers, and ensures data consistency.
- **`data_cleaning.py`**: Provides additional functions for parsing, handling malformed entries, and removing anomalies.

#### **Data Transformation**
- **`data_transformation.py`**: Includes Fourier Transform (FFT) for frequency analysis and interpolation for missing data.

#### **Data Filtering**
- **`data_filtering.py`**: Implements low-pass, high-pass, and band-pass filters to clean noisy signals.

#### **Statistical Analysis**
- **`statistical_analysis.py`**: Calculates descriptive statistics (mean, median, variance, etc.) and generates a correlation matrix.

#### **Data Visualization**
- **`time_series_plotting.py`**: Creates static and interactive time-series plots.
- **`orientation_3d_visualization.py`**: Visualizes spacecraft orientation in 3D using roll, pitch, and yaw data.

#### **Anomaly Detection**
- **`anomaly_detection.py`**: Uses Z-scores, threshold-based methods, and Isolation Forest for detecting telemetry anomalies.

#### **Orbital Analysis**
- **`orbital_analysis.py`**: Calculates Keplerian orbital elements and validates spacecraft trajectories.

#### **Power System Monitoring**
- **`power_system_monitoring.py`**: Analyzes power generation and consumption trends, detects deviations, and calculates energy balances.

#### **Attitude Control Analysis**
- **`attitude_control_analysis.py`**: Performs quaternion transformations, validates spacecraft orientation data, and compares sensor data (gyroscopes and star trackers).

#### **Thermal Analysis**
- **`thermal_analysis.py`**: Tracks temperature changes, detects anomalies, and models heat dissipation.

#### **Data Compression and Storage**
- **`data_compression_storage.py`**: Compresses datasets into GZIP, Parquet, and ZIP formats and exports analyzed data to CSV, JSON, and Excel.

---

### **2. Sample Data**
- **`sample_data.csv`**: A general sample dataset with telemetry data.
- **`orientation_sample.csv`**: Sample data for spacecraft orientation (quaternions and Euler angles).
- **`sample_power_data.csv`**: Dataset for analyzing power generation and consumption trends.
- **`sample_attitude_data.csv`**: Attitude data with quaternions for spacecraft orientation validation.
- **`sample_temperature_data.csv`**: Temperature dataset for thermal analysis.
- **`sample_gyro_data.csv`**: Gyroscope data for comparison with star tracker measurements.

---

### **3. Outputs**
- **`outputs/`**: Contains generated plots, processed data, and compressed files.
  - `plots/`: Visualization outputs (time-series, 3D orientation, thermal trends, etc.).
  - `anomalies/`: Detected anomalies in various analyses.
  - `compressed/`: Compressed datasets and archives.

---