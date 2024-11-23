# Spacecraft Data Tools

A collection of Python scripts designed for analyzing spacecraft and satellite data. These tools are tailored to process large datasets, visualize telemetry, and extract actionable insights from mission-critical data.

## Features
- Data ingestion and cleaning
- Time-series visualization
- Anomaly detection
- Orbital calculations
- Signal processing and filtering

## Getting Started
1. Fork and Clone this repository:
   ```bash
   git clone https://github.com/yourusername/spacecraft-data-tools.git
   cd spacecraft-data-tools

2. Install the required Python libraries:
  ```bash
    pip install -r requirements.txt
  ```
## Repository Structure
  ```bash
    spacecraft-data-tools/ 
    ├── README.md # Overview and instructions 
    ├── data/ # Sample datasets 
    │ ├── sample_data.csv # General telemetry data 
    │ ├── orientation_sample.csv # Orientation data (quaternions and Euler angles) 
    │ ├── sample_power_data.csv # Power system data 
    │ ├── sample_attitude_data.csv # Spacecraft attitude data 
    │ ├── sample_temperature_data.csv # Thermal analysis data 
    │ ├── sample_gyro_data.csv # Gyroscope sensor data 
    ├── scripts/ # Python scripts for data analysis 
    │ ├── data_ingestion.py # Data ingestion and parsing 
    │ ├── data_cleaning.py # Parsing and cleaning data 
    │ ├── data_transformation.py # Fourier Transform and interpolation 
    │ ├── data_filtering.py # Signal filtering (low-pass, high-pass, band-pass) 
    │ ├── statistical_analysis.py # Statistical computations and correlation matrix 
    │ ├── time_series_plotting.py # Time-series data visualization 
    │ ├── orientation_3d_visualization.py # 3D orientation visualization 
    │ ├── anomaly_detection.py # Detect anomalies in telemetry 
    │ ├── orbital_analysis.py # Calculate orbital elements and validate trajectories 
    │ ├── power_system_monitoring.py # Power generation and consumption analysis 
    │ ├── attitude_control_analysis.py # Validate orientation and sensor data 
    │ ├── thermal_analysis.py # Temperature tracking and heat dissipation modeling 
    │ ├── data_compression_storage.py # Compress datasets and export formats 
    ├── outputs/ # Example outputs (e.g., plots, summaries) 
    │ ├── anomalies/ # Detected anomalies 
    │ ├── plots/ # Visualization outputs 
    │ ├── compressed/ # Compressed datasets 
    ├── requirements.txt # Required Python libraries
  ```
---

## **Key Features**

### **Data Analysis**
- Ingest, clean, and preprocess large telemetry datasets.
- Perform statistical analysis and identify correlations.

### **Visualization**
- Create time-series and 3D orientation plots.
- Visualize temperature, power trends, and energy balances.

### **Advanced Analysis**
- Detect anomalies using Z-scores, thresholds, and Isolation Forest.
- Calculate orbital elements and validate trajectories.
- Model thermal dissipation and power system efficiency.

### **Data Management**
- Export analyzed data to CSV, JSON, or Excel formats.
- Compress datasets using GZIP, Parquet, or ZIP.

---

## **Future Enhancements**

1. **Statistical Analysis**:
   - Add percentile and quantile analysis for advanced data profiling.

2. **Time-Series Analysis**:
   - Implement moving averages (simple and exponential).
   - Include autocorrelation and lagged correlation analysis.

3. **Orbital Mechanics**:
   - Add delta-v calculations and TLE (Two-Line Element) propagation.

4. **Sensor Calibration**:
   - Create tools for bias correction and gain adjustment.

5. **Thermal Gradient Analysis**:
   - Calculate temperature rate of change and detect equilibrium/instability regions.

6. **Power Budget Calculations**:
   - Add battery charge/discharge efficiency analysis.

7. **Error Analysis**:
   - Extend scripts to include uncertainty propagation.

8. **Machine Learning Applications**:
   - Add clustering for telemetry pattern recognition and predictive modeling for spacecraft systems.

---
## Usage
- Replace the placeholder data/sample_data.csv with your dataset.
- Run the relevant script from the scripts/ folder. Example:
  ```bash
    python scripts/data_ingestion.py --file data/your_data.csv
  ```
  Note: you may nead to use 'python3' instead of python depending on your system.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## **Future Enhancements**

1. **Statistical Analysis**:
   - Add percentile and quantile analysis for advanced data profiling.

2. **Time-Series Analysis**:
   - Implement moving averages (simple and exponential).
   - Include autocorrelation and lagged correlation analysis.

3. **Orbital Mechanics**:
   - Add delta-v calculations and TLE (Two-Line Element) propagation.

4. **Sensor Calibration**:
   - Create tools for bias correction and gain adjustment.

5. **Thermal Gradient Analysis**:
   - Calculate temperature rate of change and detect equilibrium/instability regions.

6. **Power Budget Calculations**:
   - Add battery charge/discharge efficiency analysis.

7. **Error Analysis**:
   - Extend scripts to include uncertainty propagation.

8. **Machine Learning Applications**:
   - Add clustering for telemetry pattern recognition and predictive modeling for spacecraft systems.

---

