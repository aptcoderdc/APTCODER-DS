import random

# Generate a list of 30 random daily temperatures between 20°C and 35°C
temperatures = [random.randint(20, 35) for _ in range(30)]
print("Daily Temperatures:", temperatures)

# Simple moving average forecasting
def moving_average_forecast(temps, window_size):
    forecasted_temps = []
    for i in range(window_size, len(temps)):
        avg_temp = sum(temps[i-window_size:i]) / window_size
        forecasted_temps.append(avg_temp)
    return forecasted_temps

# Forecast the next day's temperature based on the last 3 days
forecasted_temps = moving_average_forecast(temperatures, 3)
print("Forecasted Temperatures:", forecasted_temps)

# Anomaly detection
def detect_anomalies(temps, forecasted_temps, window_size, threshold):
    anomalies = []
    for i in range(window_size, len(temps)):
        if abs(temps[i] - forecasted_temps[i-window_size]) > threshold:
            anomalies.append((i, temps[i]))
    return anomalies

# Detect anomalies with a threshold of 5°C
anomalies = detect_anomalies(temperatures, forecasted_temps, 3, 5)
print("Anomalies:", anomalies)
