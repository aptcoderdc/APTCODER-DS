import pandas as pd
import random  # Make sure to import the random module

# Sample dataset: A DataFrame of employee records
data = {
    "Name": ["Alice", "Bob", "Charlie", "Daisy", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Gender": ["Female", "Male", "Male", "Female", "Female", "Male", "Female", "Female", "Male", "Male"],
    "Ethnicity": ["Group A", "Group B", "Group A", "Group B", "Group A", "Group B", "Group A", "Group B", "Group A", "Group B"],
    "Salary": [60000, 55000, 62000, 59000, 64000, 58000, 67000, 61000, 56000, 63000],
    "Age": [25, 30, 28, 27, 29, 31, 24, 26, 32, 29]
}

df = pd.DataFrame(data)

# Display the original dataset
print("Original Dataset:")
print(df)

# Privacy Concerns: Identifying Sensitive Information
def identify_sensitive_information(df):
    sensitive_columns = ["Name", "Salary"]
    print("\nSensitive Information Detected:")
    for column in sensitive_columns:
        print(f"Column '{column}' may contain sensitive information.")
    return sensitive_columns

identify_sensitive_information(df)

# Privacy Protection: Anonymizing the Data
def anonymize_data(df):
    df_anonymized = df.copy()
    df_anonymized["Name"] = ["Person" + str(i+1) for i in range(len(df))]
    df_anonymized["Salary"] = df_anonymized["Salary"].apply(lambda x: x + random.randint(-5000, 5000))  # Add noise
    return df_anonymized

df_anonymized = anonymize_data(df)

# Display the anonymized dataset
print("\nAnonymized Dataset:")
print(df_anonymized)

# Evaluating Privacy Protection
def evaluate_privacy_protection(original_df, anonymized_df):
    original_salary_mean = original_df["Salary"].mean()
    anonymized_salary_mean = anonymized_df["Salary"].mean()
    privacy_protection_effectiveness = abs(original_salary_mean - anonymized_salary_mean)
    print(f"\nEffectiveness of Privacy Protection:")
    print(f"Mean Salary Difference: {privacy_protection_effectiveness}")

evaluate_privacy_protection(df, df_anonymized)

# Bias Analysis in Anonymized Data: Gender Bias
def calculate_average_salary_by_gender(df):
    gender_salaries = df.groupby("Gender")["Salary"].mean()
    return gender_salaries

average_salary_by_gender_anonymized = calculate_average_salary_by_gender(df_anonymized)
print("\nAverage Salary by Gender (Anonymized Data):")
print(average_salary_by_gender_anonymized)

# Detecting Bias
def detect_gender_bias(average_salary_by_gender):
    if average_salary_by_gender["Male"] > average_salary_by_gender["Female"]:
        return "Bias detected: Male employees have higher average salaries."
    elif average_salary_by_gender["Male"] < average_salary_by_gender["Female"]:
        return "Bias detected: Female employees have higher average salaries."
    else:
        return "No significant bias detected."

gender_bias_detection = detect_gender_bias(average_salary_by_gender_anonymized)
print(gender_bias_detection)
