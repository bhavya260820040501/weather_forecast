import joblib
import matplotlib.pyplot as plt
from preprocess import preprocess_data

# Load the preprocessed data
file_path = "../data/powerconsumption.csv"
data = preprocess_data(file_path)

# Define features and target
features = ['Temperature', 'Humidity', 'WindSpeed', 'GeneralDiffuseFlows', 'DiffuseFlows']
target = 'PowerConsumption_Zone1'

X = data[features]
y = data[target]

# Load the saved model
model = joblib.load('../models/power_consumption_model.pkl')

# Make predictions
y_pred = model.predict(X)

# Plot actual vs predicted
plt.figure(figsize=(10, 6))
plt.plot(y.index, y, label='Actual', color='blue')
plt.plot(y.index, y_pred, label='Predicted', color='red')
plt.xlabel('Datetime')
plt.ylabel('Power Consumption (Zone 1)')
plt.title('Actual vs Predicted Power Consumption')
plt.legend()
plt.show()