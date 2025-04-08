import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "../data/powerconsumption.csv"
data = pd.read_csv(file_path)

# Display the first few rows
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Check data types
print(data.info())

# Convert 'Datetime' to datetime object and set as index
data['Datetime'] = pd.to_datetime(data['Datetime'], format='%m/%d/%Y %H:%M')  # Corrected format
data.set_index('Datetime', inplace=True)

# Plot Power Consumption Zone 1
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['PowerConsumption_Zone1'], label='Zone 1 Power Consumption')
plt.xlabel('Datetime')
plt.ylabel('Power Consumption')
plt.title('Power Consumption Over Time')
plt.legend()
plt.show()