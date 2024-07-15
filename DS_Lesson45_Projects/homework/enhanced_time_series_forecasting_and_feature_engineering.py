import random

# Use the same list of daily temperatures from the project
temperatures = [random.randint(20, 35) for _ in range(30)]
print("Daily Temperatures:", temperatures)

# Weighted moving average forecasting
def weighted_moving_average_forecast(temps, window_size):
    forecasted_temps = []
    weights = [i for i in range(1, window_size+1)]
    weight_sum = sum(weights)
    for i in range(window_size, len(temps)):
        weighted_sum = sum(temps[i-window_size+j] * weights[j] for j in range(window_size))
        avg_temp = weighted_sum / weight_sum
        forecasted_temps.append(avg_temp)
    return forecasted_temps

# Forecast the next day's temperature based on a weighted average of the last 3 days
forecasted_temps = weighted_moving_average_forecast(temperatures, 3)
print("Forecasted Temperatures:", forecasted_temps)

# Feature engineering: temperature difference from the previous day
def temp_differences(temps):
    differences = [temps[i] - temps[i-1] for i in range(1, len(temps))]
    return differences

temp_diffs = temp_differences(temperatures)
print("Temperature Differences:", temp_diffs)

# Anomaly detection using temperature differences
def detect_anomalies_with_features(temps, forecasted_temps, temp_diffs, window_size, threshold):
    anomalies = []
    for i in range(window_size, len(temps)):
        if abs(temps[i] - forecasted_temps[i-window_size]) > threshold or abs(temp_diffs[i-window_size-1]) > threshold:
            anomalies.append((i, temps[i]))
    return anomalies

# Detect anomalies with a threshold of 5°C
anomalies = detect_anomalies_with_features(temperatures, forecasted_temps, temp_diffs, 3, 5)
print("Anomalies:", anomalies)
