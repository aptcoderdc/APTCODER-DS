import random

# Sample dataset: A list of student records
students = [
    {"name": "Alice", "gender": "Female", "score": 85},
    {"name": "Bob", "gender": "Male", "score": 78},
    {"name": "Charlie", "gender": "Male", "score": 82},
    {"name": "Daisy", "gender": "Female", "score": 90},
    {"name": "Eva", "gender": "Female", "score": 88},
    {"name": "Frank", "gender": "Male", "score": 76},
    {"name": "Grace", "gender": "Female", "score": 95},
    {"name": "Hannah", "gender": "Female", "score": 80},
    {"name": "Ian", "gender": "Male", "score": 72},
    {"name": "Jack", "gender": "Male", "score": 89}
]

# Analyzing Bias: Gender Bias in Average Scores
def calculate_average_score_by_gender(students):
    gender_scores = {"Male": [], "Female": []}
    for student in students:
        gender_scores[student["gender"]].append(student["score"])
    average_scores = {gender: sum(scores)/len(scores) for gender, scores in gender_scores.items()}
    return average_scores

average_scores_by_gender = calculate_average_score_by_gender(students)
print("Average Scores by Gender:", average_scores_by_gender)

# Detecting Bias
def detect_bias(average_scores_by_gender):
    if average_scores_by_gender["Male"] > average_scores_by_gender["Female"]:
        return "Bias detected: Male students have higher average scores."
    elif average_scores_by_gender["Male"] < average_scores_by_gender["Female"]:
        return "Bias detected: Female students have higher average scores."
    else:
        return "No significant bias detected."

bias_detection = detect_bias(average_scores_by_gender)
print(bias_detection)

# Mitigating Bias: Adjusting Scores
def adjust_scores_for_fairness(students):
    average_scores_by_gender = calculate_average_score_by_gender(students)
    gender_correction = {gender: 85 - average for gender, average in average_scores_by_gender.items()}
    adjusted_students = []
    for student in students:
        adjusted_score = student["score"] + gender_correction[student["gender"]]
        adjusted_students.append({"name": student["name"], "gender": student["gender"], "score": adjusted_score})
    return adjusted_students

adjusted_students = adjust_scores_for_fairness(students)
adjusted_average_scores_by_gender = calculate_average_score_by_gender(adjusted_students)
print("Adjusted Average Scores by Gender:", adjusted_average_scores_by_gender)

# Evaluating Fairness After Adjustment
def evaluate_fairness(average_scores_by_gender, adjusted_average_scores_by_gender):
    return average_scores_by_gender, adjusted_average_scores_by_gender

print("Bias Before Adjustment:", average_scores_by_gender)
print("Bias After Adjustment:", adjusted_average_scores_by_gender)
