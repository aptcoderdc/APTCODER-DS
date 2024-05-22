# Importing necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data: Favorite fruits of classmates
data = {
    'Fruits': ['Apple', 'Banana', 'Orange', 'Grapes', 'Strawberry'],
    'Votes': [10, 6, 8, 4, 2]
}

# Create a bar chart
def create_bar_chart(data):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=data['Fruits'], y=data['Votes'], palette='viridis')
    plt.title('Favorite Fruits in the Classroom')
    plt.xlabel('Fruits')
    plt.ylabel('Number of Votes')
    plt.show()

# Create a pie chart
def create_pie_chart(data):
    plt.figure(figsize=(8, 8))
    plt.pie(data['Votes'], labels=data['Fruits'], autopct='%1.1f%%', colors=sns.color_palette('viridis'))
    plt.title('Favorite Fruits in the Classroom')
    plt.show()

# Call the functions to create the charts
create_bar_chart(data)
create_pie_chart(data)
