import pandas as pd

# Load the dataset
data = pd.read_csv('school_attendance.csv')

# Calculate total days for each student
data['Total Days'] = data['Days Present'] + data['Days Absent']

# Calculate attendance percentage
data['Attendance Percentage'] = (data['Days Present'] / data['Total Days']) * 100

# Print the data with attendance percentage
print(data)

# Find average attendance percentage
avg_attendance = data['Attendance Percentage'].mean()
print(f"Average Attendance Percentage: {avg_attendance:.2f}%")

import matplotlib.pyplot as plt

# Plot attendance percentage
plt.figure(figsize=(10, 6))
plt.bar(data['Student'], data['Attendance Percentage'], color='skyblue')
plt.xlabel('Student')
plt.ylabel('Attendance Percentage')
plt.title('Attendance Percentage of Students')
plt.show()
