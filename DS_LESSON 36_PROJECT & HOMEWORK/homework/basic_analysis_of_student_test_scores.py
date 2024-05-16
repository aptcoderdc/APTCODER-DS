import pandas as pd

    # Load the dataset
data = pd.read_csv('test_scores.csv')

    # Calculate average scores for each subject
avg_math = data['Math'].mean()
avg_science = data['Science'].mean()
avg_english = data['English'].mean()

    # Find highest and lowest scores for each subject
max_math = data['Math'].max()
min_math = data['Math'].min()
max_science = data['Science'].max()
min_science = data['Science'].min()
max_english = data['English'].max()
min_english = data['English'].min()

    # Print results
print(f"Average Math Score: {avg_math}")
print(f"Highest Math Score: {max_math}, Lowest Math Score: {min_math}")
print(f"Average Science Score: {avg_science}")
print(f"Highest Science Score: {max_science}, Lowest Science Score: {min_science}")
print(f"Average English Score: {avg_english}")
print(f"Highest English Score: {max_english}, Lowest English Score: {min_english}")