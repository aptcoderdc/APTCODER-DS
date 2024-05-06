import matplotlib.pyplot as plt

# Sample data
subjects = ['Math', 'Science', 'English', 'History', 'Art']
num_students = [20, 15, 12, 8, 10]

# Creating the pie chart
plt.pie(num_students, labels=subjects, autopct='%1.1f%%', startangle=140)

# Adding title
plt.title('Favorite Subjects of Students')

# Displaying the pie chart
plt.show()
