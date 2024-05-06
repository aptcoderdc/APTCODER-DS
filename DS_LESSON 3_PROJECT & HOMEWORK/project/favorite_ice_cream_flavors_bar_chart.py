import matplotlib.pyplot as plt

# Sample data of favorite ice cream flavors and number of students
ice_cream_flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint']
num_students = [15, 12, 10, 8]

# Creating the bar chart
plt.bar(ice_cream_flavors, num_students, color='skyblue')

# Adding labels and title
plt.xlabel('Ice Cream Flavors')
plt.ylabel('Number of Students')
plt.title('Favorite Ice Cream Flavors')

# Displaying the bar chart
plt.show()
