# Data Science in Agriculture: Analyzing Agricultural Data for Crop Management and Optimization

## Introduction

This project demonstrates how to use data science techniques to analyze agricultural data for improving crop management and optimizing crop yields. The dataset used in this project is manually created within the script, simulating typical agricultural data including temperature, precipitation, soil quality, and crop yield.

## Project Structure

The project is structured as follows:
1. **Data Acquisition**: Creation of a sample dataset.
2. **Data Preprocessing**: Handling missing values and feature engineering.
3. **Exploratory Data Analysis (EDA)**: Visualizing data to understand patterns and correlations.
4. **Modeling**: Building and evaluating a linear regression model.
5. **Optimization and Prediction**: Using the model for predictions and optimization of crop yields.
6. **Conclusion**: Summarizing findings and future work.

## Setup and Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Pandas
- Seaborn
- Matplotlib
- Scikit-learn

You can install the required libraries using pip:
```sh
pip install pandas seaborn matplotlib scikit-learn
Running the Project
Clone the repository or download the project files.
Navigate to the project directory.
Run the Python script:
sh

python agricultural_data_analysis.py
Code Overview
Data Acquisition
A sample dataset is created directly within the script using pandas DataFrame.

Data Preprocessing
Fill missing values using forward fill method.
Create a new feature temp_precip_interaction representing the interaction between temperature and precipitation.
Exploratory Data Analysis (EDA)
Visualize data relationships using pair plots.
Compute and visualize the correlation matrix using a heatmap.
Modeling
Split the data into training and testing sets.
Train a linear regression model using the training data.
Evaluate the model using Mean Squared Error (MSE) and R² Score.
Optimization and Prediction
Use the trained model to predict crop yields based on new input conditions.