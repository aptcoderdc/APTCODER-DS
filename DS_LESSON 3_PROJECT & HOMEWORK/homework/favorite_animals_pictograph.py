import matplotlib.pyplot as plt

# Sample data of favorite animals and number of students
animals = ['Dog', 'Cat', 'Bird', 'Fish']
num_students = [20, 15, 10, 5]

# Creating the pictograph
plt.figure(figsize=(8, 6))
for i in range(len(animals)):
    plt.scatter(i, 0, s=num_students[i]*100, label=animals[i], alpha=0.5)

# Adding labels and title
plt.title('Favorite Animals Pictograph')
plt.xlabel('Animals')
plt.ylabel('Number of Students')

# Creating a legend
plt.legend(loc='upper right')

# Setting x-axis ticks and labels
plt.xticks(range(len(animals)), animals)

# Displaying the pictograph
plt.show()
