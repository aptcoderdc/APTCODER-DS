# Favorite Fruits Data Visualization

This project is designed to teach kids how to visualize data by creating bar charts and pie charts using Python. The example data represents a survey of classmates' favorite fruits.

## Project Overview

The project involves:
- Collecting data on favorite fruits.
- Creating a bar chart to visualize the number of votes each fruit received.
- Creating a pie chart to visualize the distribution of votes among the fruits.

## Prerequisites

Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

You will also need to install the following Python libraries:
- `matplotlib`
- `seaborn`

You can install these libraries using `pip`:

```sh
pip install matplotlib seaborn
How to Run the Project
Download or Clone the Repository:

You can download the project files as a ZIP or clone the repository using git:


git clone https://github.com/yourusername/favorite-fruits-visualization.git
Navigate to the Project Directory:

Open a terminal or command prompt and navigate to the directory where you saved the project files:


cd favorite-fruits-visualization
Run the Python Script:

Execute the script to generate and display the charts:


python favorite_fruits.py
Project Files
favorite_fruits.py: The main script that contains the code for generating the bar chart and pie chart.

Code Explanation
The script imports the necessary libraries, defines sample data for the favorite fruits survey, and includes functions to create and display bar and pie charts.

Importing Libraries

import matplotlib.pyplot as plt
import seaborn as sns
Sample Data

data = {
    'Fruits': ['Apple', 'Banana', 'Orange', 'Grapes', 'Strawberry'],
    'Votes': [10, 6, 8, 4, 2]
}
Creating the Bar Chart

def create_bar_chart(data):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=data['Fruits'], y=data['Votes'], palette='viridis')
    plt.title('Favorite Fruits in the Classroom')
    plt.xlabel('Fruits')
    plt.ylabel('Number of Votes')
    plt.show()
Creating the Pie Chart

def create_pie_chart(data):
    plt.figure(figsize=(8, 8))
    plt.pie(data['Votes'], labels=data['Fruits'], autopct='%1.1f%%', colors=sns.color_palette('viridis'))
    plt.title('Favorite Fruits in the Classroom')
    plt.show()
Displaying the Charts

create_bar_chart(data)
create_pie_chart(data)
Customization
Feel free to modify the data or customize the charts to make the project your own. You can change the fruits, the number of votes, or the colors used in the charts.

