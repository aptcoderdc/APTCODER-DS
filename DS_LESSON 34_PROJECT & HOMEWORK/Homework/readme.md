# Optimizing Public Transportation Schedules Based on Passenger Demand

## Overview

This project aims to optimize public transportation schedules by analyzing passenger demand patterns. By clustering timestamps with passenger counts, we can identify different demand patterns throughout the day and adjust transportation schedules accordingly to improve efficiency and passenger satisfaction.

## Project Structure

- `generate_data.py`: Python script to generate synthetic public transportation data, including timestamps and passenger counts.
- `preprocess_data.py`: Python script to preprocess the generated data, extracting relevant features such as hour, minute, and passenger count.
- `cluster_demand.py`: Python script to perform clustering on the preprocessed data to identify demand patterns.
- `analyze_demand.py`: Python script to analyze demand patterns by visualizing histograms of passenger counts for each cluster.
- `optimize_schedules.py`: Python script to optimize transportation schedules based on the identified demand patterns.

## Usage

1. **Generate Data**: Run `generate_data.py` to generate synthetic public transportation data.

    ```
    python generate_data.py
    ```

2. **Preprocess Data**: Run `preprocess_data.py` to preprocess the generated data.

    ```
    python preprocess_data.py
    ```

3. **Cluster Demand**: Run `cluster_demand.py` to perform clustering on the preprocessed data.

    ```
    python cluster_demand.py
    ```

4. **Analyze Demand**: Run `analyze_demand.py` to analyze demand patterns by visualizing histograms.

    ```
    python analyze_demand.py
    ```

5. **Optimize Schedules**: Run `optimize_schedules.py` to optimize transportation schedules based on demand patterns.

    ```
    python optimize_schedules.py
    ```

## Requirements

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- scikit-learn