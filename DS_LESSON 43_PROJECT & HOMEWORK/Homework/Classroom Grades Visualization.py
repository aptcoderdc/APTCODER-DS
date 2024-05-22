# Importing necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data: Grades of classmates
grades = [85, 92, 88, 75, 69, 95, 80, 78, 91, 85, 89, 74, 82, 90, 77, 84, 93, 79, 81, 76]

# Create a histogram
def create_histogram(grades):
    plt.figure(figsize=(10, 6))
    sns.histplot(grades, bins=10, kde=True, color='blue')
    plt.title('Distribution of Grades in the Classroom')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.show()

# Create a box plot
def create_box_plot(grades):
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=grades, color='green')
    plt.title('Box Plot of Grades in the Classroom')
    plt.ylabel('Grades')
    plt.show()

# Call the functions to create the charts
create_histogram(grades)
create_box_plot(grades)
