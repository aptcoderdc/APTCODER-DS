import random

# Generate a list of 50 random crime incidents
crime_types = ["Theft", "Assault", "Robbery", "Burglary", "Vandalism"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

crime_data = []
for _ in range(50):
    crime = {
        "date": random.choice(days_of_week),
        "type": random.choice(crime_types),
        "location": "Location " + str(random.randint(1, 10))
    }
    crime_data.append(crime)

print("Crime Data:", crime_data)

# Data visualization: Bar chart of crime types
def crime_type_count(crime_data):
    type_count = {crime: 0 for crime in crime_types}
    for incident in crime_data:
        type_count[incident["type"]] += 1
    return type_count

type_count = crime_type_count(crime_data)
print("Crime Type Count:", type_count)

# Detecting patterns
def most_common_crime(type_count):
    return max(type_count, key=type_count.get)

def crimes_per_day(crime_data):
    day_count = {day: 0 for day in days_of_week}
    for incident in crime_data:
        day_count[incident["date"]] += 1
    return day_count

day_count = crimes_per_day(crime_data)
print("Crimes Per Day:", day_count)

most_common = most_common_crime(type_count)
most_frequent_day = most_common_crime(day_count)

print("Most Common Crime:", most_common)
print("Most Frequent Day for Crimes:", most_frequent_day)
