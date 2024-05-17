# Final Project: Analyzing School Performance Data

## Overview
This project combines various data science concepts to analyze school performance data. Students will clean the data, perform exploratory data analysis, apply regression and classification techniques, and visualize the results.

## Concepts Covered
- Data Cleaning
- Exploratory Data Analysis
- Regression Analysis
- Classification
- Data Visualization

## Required Libraries
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Setup
1. Install Python if you haven't already. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required libraries:
    ```
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```

## How to Run
1. Clone or download the project repository to your local machine.
2. Ensure the `school_performance.csv` file is in the same directory as the script.
3. Run the `school_performance_analysis.py` file using Python:
    ```
    python school_performance_analysis.py
    ```

## Example Output

Summary Statistics:
Grade Math Score Reading Score Science Score Days Present Days Absent
count 6.0 6.000000 6.000000 6.000000 6.000000 6.000000
mean 6.5 82.166667 79.666667 86.500000 178.333333 6.666667
std 0.5 11.737217 9.272815 10.676319 5.164859 5.164859
min 6.0 65.000000 68.000000 70.000000 170.000000 0.000000
25% 6.0 75.000000 73.500000 80.000000 175.000000 3.000000
50% 6.5 81.500000 78.000000 91.000000 179.000000 6.000000
75% 7.0 89.250000 88.000000 94.250000 182.000000 10.000000
max 7.0 98.000000 92.000000 95.000000 185.000000 15.000000

Model Coefficients: [ 0.05 -0.03 0.02]
Model Intercept: 5.50

Classification Accuracy: 1.0