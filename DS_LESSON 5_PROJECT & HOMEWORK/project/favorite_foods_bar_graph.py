import matplotlib.pyplot as plt

# Sample data
foods = ['Pizza', 'Burger', 'Pasta', 'Sandwich', 'Ice Cream']
num_students = [15, 10, 8, 12, 7]

# Creating the bar graph
plt.bar(foods, num_students, color='skyblue')

# Adding labels and title
plt.xlabel('Favorite Foods')
plt.ylabel('Number of Students')
plt.title('Favorite Foods of Students')

# Displaying the bar graph
plt.show()
