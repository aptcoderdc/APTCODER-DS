import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('student_performance.csv')

# Print dataset summary
print("Dataset Summary:\n", data.describe())

# Calculate average scores for each subject
avg_math = data['Math'].mean()
avg_science = data['Science'].mean()
avg_english = data['English'].mean()

print(f"Average Math Score: {avg_math}")
print(f"Average Science Score: {avg_science}")
print(f"Average English Score: {avg_english}")

# Plot average scores
subjects = ['Math', 'Science', 'English']
averages = [avg_math, avg_science, avg_english]

plt.bar(subjects, averages, color=['blue', 'green', 'red'])
plt.xlabel('Subjects')
plt.ylabel('Average Scores')
plt.title('Average Scores by Subject')
plt.show()
