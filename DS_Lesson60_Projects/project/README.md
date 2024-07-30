
# Comprehensive Data Analysis and Prediction System

## Overview

The **Comprehensive Data Analysis and Prediction System** is a project that demonstrates end-to-end data analysis and predictive modeling. The project includes generating synthetic data, exploratory data analysis (EDA), preprocessing, training multiple machine learning models, and visualizing the results interactively.

## Features

- **Synthetic Data Generation**: Creates a dataset with features including patient age, pollution level, crime rate, star brightness, and robot sensor values.
- **Exploratory Data Analysis (EDA)**: Provides a pairwise plot to understand the relationships between features and target variable.
- **Data Preprocessing**: Scales numerical features using `StandardScaler`.
- **Model Training**: Trains and evaluates three machine learning models: RandomForest, SVM, and DecisionTree.
- **Interactive Visualization**: Plots predictions against features using Plotly for an interactive experience.

## Prerequisites

- Python 3.x
- Required libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `plotly`

You can install the necessary libraries using pip:

pip install pandas numpy matplotlib seaborn scikit-learn plotly

## Usage

1. **Generate Synthetic Data**

   The `generate_data` function creates a synthetic dataset with 1000 records and saves it as `synthetic_data.csv`.

2. **Load and Explore Data**

   The dataset is loaded from `synthetic_data.csv` and visualized using pairwise plots.

3. **Preprocess Data**

   The features are scaled using `StandardScaler` and the data is split into training and testing sets.

4. **Train and Evaluate Models**

   Three models are trained and evaluated:
   - `RandomForestClassifier`
   - `SVC`
   - `DecisionTreeClassifier`

   The evaluation includes confusion matrices and classification reports for each model.

5. **Interactive Visualization**

   Predictions made by the RandomForest model are plotted interactively using Plotly, showing how predictions relate to features like pollution level and star brightness.

## Files

- `comprehensive_data_analysis_and_prediction_system.py`: Contains the code for generating data, EDA, preprocessing, training models, and visualizing results.
- `synthetic_data.csv`: The synthetic dataset created by the project.

## Example

To run the project, execute the script `comprehensive_data_analysis_and_prediction_system.py` or `final_project`.py`:

python comprehensive_data_analysis_and_prediction_system.py

This will generate the dataset, perform EDA, preprocess the data, train the models, and display the results and interactive visualizations.

