# Analyzing and Mitigating Bias in a Dataset

## Overview
In this project, you will work with a dataset to identify biases, analyze how these biases affect outcomes, and apply strategies to mitigate them. You will use a sample dataset of student records to explore different types of bias and fairness in data science.

## Concepts Covered
- Bias Detection
- Fairness in Data Science
- Adjusting for Bias
- Evaluating Fairness

## Required Libraries
- Python Standard Library (no external libraries required)

## Setup
1. Ensure you have Python 2 installed on your system.
2. Open Visual Studio Code (VS Code).
3. Create a new directory for the project and navigate into it.
4. Create a Python file named `project.py` and copy the provided code into this file.

## How to Run
1. Open `project.py` in VS Code.
2. Run the file by pressing `Ctrl + F5` or using the Run command from the menu.

## Example Output

Average Scores by Gender: {'Male': 78.5, 'Female': 86.66666666666667}
Bias Detected: Female students have higher average scores.
Adjusted Average Scores by Gender: {'Male': 85.0, 'Female': 85.0}
Bias Before Adjustment: {'Male': 78.5, 'Female': 86.66666666666667}
Bias After Adjustment: {'Male': 85.0, 'Female': 85.0}
