
# Data Science Analysis and Model Enhancement

## Overview

The **Data Science Analysis and Model Enhancement** homework involves generating synthetic data, handling missing values, preprocessing, hyperparameter tuning, and model evaluation. This project focuses on enhancing a RandomForestClassifier model by fine-tuning its parameters and evaluating its performance.

## Features

- **Synthetic Data Generation**: Creates a dataset with features such as patient age, pollution level, crime rate, star brightness, and robot sensor values.
- **Data Modification**: Introduces missing values into the dataset for testing imputation techniques.
- **Data Preprocessing**: Handles missing values using `SimpleImputer` and scales features using `StandardScaler`.
- **Hyperparameter Tuning**: Uses `GridSearchCV` to find the best hyperparameters for the RandomForestClassifier.
- **Model Evaluation**: Evaluates the best model using confusion matrix and classification report.
- **Feature Importance Plotting**: Visualizes feature importances of the trained RandomForest model.

## Prerequisites

- Python 3.x
- Required libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `scikit-learn`

You can install the necessary libraries using pip:

pip install pandas numpy matplotlib scikit-learn

## Usage

1. **Generate and Modify Data**

   The `generate_data` function creates a synthetic dataset. The `modify_data` function introduces missing values into the dataset.

2. **Preprocess Data**

   The dataset is preprocessed by imputing missing values and scaling features.

3. **Hyperparameter Tuning**

   `GridSearchCV` is used to find the best hyperparameters for the RandomForestClassifier. The best parameters are printed.

4. **Train and Evaluate Model**

   The best RandomForest model is trained and evaluated. The confusion matrix and classification report are printed.

5. **Plot Feature Importance**

   The importance of each feature in the trained RandomForest model is plotted to visualize their contribution.

## Files

- `data_science_analysis_and_model_enhancement.py`: Contains the code for generating and modifying data, preprocessing, hyperparameter tuning, model evaluation, and plotting feature importance.

## Example

To run the homework, execute the script `data_science_analysis_and_model_enhancement.py` or `final_homework.py`:

python data_science_analysis_and_model_enhancement.py

This will generate the dataset, modify it, preprocess the data, perform hyperparameter tuning, evaluate the model, and display the feature importance plot.
