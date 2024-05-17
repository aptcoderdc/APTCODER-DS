# Advanced Product Sales Analysis

## Overview
This homework involves performing advanced data analysis and visualization on a dataset related to product sales. Students will learn how to load data, calculate summary statistics, visualize data, and explore correlations.

## Concepts Covered
- Basic data analysis
- Calculating averages and identifying maximum values
- Data visualization using bar plots and scatter plots
- Correlation analysis

## Required Libraries
- pandas
- matplotlib
- seaborn

## Setup
1. Install Python if you haven't already. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required libraries:
    ```
    pip install pandas matplotlib seaborn
    ```

## How to Run
1. Clone or download the project repository to your local machine.
2. Ensure the `product_sales.csv` file is in the same directory as the script.
3. Run the `advanced_product_sales_analysis.py` file using Python:
    ```
    python advanced_product_sales_analysis.py
    ```

## Example Output

First few rows of the dataset:
Product Rating Price Sales
0 Product A 4 10 500
1 Product B 3 20 300
2 Product C 5 15 700
3 Product D 4 10 450
4 Product E 2 8 200

Summary Statistics:
Rating Price Sales
count 6.000000 6.000000 6.000000
mean 3.833333 14.666667 466.666667
std 1.472244 6.837397 196.011347
min 2.000000 8.000000 200.000000
25% 3.250000 10.000000 375.000000
50% 4.000000 12.500000 475.000000
75% 4.750000 17.500000 612.500000
max 5.000000 25.000000 700.000000

Average Rating: 3.83
Total Sales: 2800
Average Price: 14.67
Product with the Highest Sales: Product C (700 units)
Product with the Highest Rating: Product C (5 stars)
Correlation between Price and Sales: -0.03
Correlation between Rating and Sales: 0.69

Average Sales by Rating:
Rating Sales
0 2 200.0
1 3 300.0
2 4 475.0
3 5 675.0

Average Sales by Price Range:
Price Range Sales
0 Low 383.3
1 Medium 500.0
2 High 300.0