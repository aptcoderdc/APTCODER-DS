# Step 1: Data Preprocessing
import pandas as pd
import matplotlib.pyplot as plt

# Simulated brain activity data
data = {
    'Time (s)': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Alpha Waves': [30, 35, 33, 32, 36, 38, 40, 39, 37, 35],
    'Beta Waves': [15, 18, 16, 17, 19, 21, 20, 22, 23, 21],
    'Gamma Waves': [5, 6, 5, 7, 8, 9, 10, 11, 12, 10]
}

df = pd.DataFrame(data)

# Plotting brain wave patterns
plt.figure(figsize=(10, 6))
plt.plot(df['Time (s)'], df['Alpha Waves'], label='Alpha Waves', marker='o')
plt.plot(df['Time (s)'], df['Beta Waves'], label='Beta Waves', marker='o')
plt.plot(df['Time (s)'], df['Gamma Waves'], label='Gamma Waves', marker='o')
plt.xlabel('Time (s)')
plt.ylabel('Wave Intensity')
plt.title('Brain Wave Patterns Over Time')
plt.legend()
plt.grid(True)
plt.savefig('brain_waves.png')
plt.show()
