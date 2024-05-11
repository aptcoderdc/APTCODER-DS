import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('student_data.csv')

# Data Cleaning
# For simplicity, we'll assume the dataset is clean

# Data Analysis
grades_mean = data['Grade'].mean()
attendance_median = data['Attendance'].median()
activities_mode = data['Activities'].mode()[0]

# Data Visualization
plt.figure(figsize=(10, 6))

# Pie Chart for Activities
plt.subplot(1, 2, 1)
activities_count = data['Activities'].value_counts()
plt.pie(activities_count, labels=activities_count.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Distribution of Extracurricular Activities')

# Bar Chart for Grades
plt.subplot(1, 2, 2)
grade_counts = data['Grade'].value_counts().sort_index()
plt.bar(grade_counts.index, grade_counts.values, color='skyblue')
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Distribution of Grades')

plt.tight_layout()
plt.show()

# Output
print("Mean Grade:", grades_mean)
print("Median Attendance:", attendance_median)
print("Mode of Activities:", activities_mode)
