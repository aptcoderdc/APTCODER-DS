# Classroom Grades Visualization

This project visualizes the distribution of grades in a classroom using a histogram and a box plot. It aims to teach kids how to use data visualization techniques to understand and interpret data.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Description](#project-description)
- [Data](#data)
- [Functions](#functions)
- [Customization](#customization)
- [License](#license)

## Introduction

Data visualization is a powerful tool for understanding and interpreting data. This project demonstrates how to create a histogram and a box plot to visualize the distribution of grades in a classroom. It is designed to be simple and educational, making it suitable for kids and beginners.

## Requirements

- Python 3.x
- `matplotlib` library
- `seaborn` library

## Installation

1. Ensure Python is installed on your computer. You can download it from [python.org](https://www.python.org/).
2. Install the necessary libraries using pip:
   ```sh
   pip install matplotlib seaborn
Usage
Save the script in a file named classroom_grades.py.
Open a terminal or command prompt, navigate to the directory where you saved the file, and run:
sh

python classroom_grades.py
This will generate and display both the histogram and the box plot showing the distribution of grades in the classroom.

Project Description
This project contains two main visualizations:

Histogram: Shows the frequency distribution of grades.
Box Plot: Provides a summary of the grades, including the median, quartiles, and potential outliers.
Data
The sample data used in this project represents the grades of classmates:


grades = [85, 92, 88, 75, 69, 95, 80, 78, 91, 85, 89, 74, 82, 90, 77, 84, 93, 79, 81, 76]
Functions
create_histogram(grades): Creates and displays a histogram of the grades.
create_box_plot(grades): Creates and displays a box plot of the grades.
Customization
Data: Modify the grades list to include different data points.
Histogram: Adjust the number of bins by changing the bins parameter in the sns.histplot function.
Colors: Customize the colors by changing the color parameter in the sns.histplot and sns.boxplot functions.