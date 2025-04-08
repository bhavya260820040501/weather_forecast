# Energy Consumption Forecasting

## Project Overview
This project focuses on forecasting energy consumption using historical data and machine learning techniques. The goal is to predict energy usage in different zones based on environmental and solar radiation data. The project uses a Linear Regression model for forecasting.

---

## Dataset
- **Name**: Electric Power Consumption Dataset
- **Source**: Kaggle
- **Features**:
  - `Datetime`: Timestamp of the observation.
  - `Temperature`: Ambient temperature in degrees Celsius.
  - `Humidity`: Relative humidity percentage.
  - `WindSpeed`: Wind speed in m/s.
  - `GeneralDiffuseFlows`: General diffuse solar radiation.
  - `DiffuseFlows`: Diffuse solar radiation.
  - `PowerConsumption_Zone1`: Energy consumption in Zone 1.
  - `PowerConsumption_Zone2`: Energy consumption in Zone 2.
  - `PowerConsumption_Zone3`: Energy consumption in Zone 3.

---

## Project Structure
H:\ai_ml_mini_project ├── data │ └── powerconsumption.csv # Dataset ├── notebooks │ └── data_exploration.py # Data exploration script ├── src │ ├── preprocess.py # Preprocessing script │ ├── train_model.py # Model training script │ └── evaluate_model.py # Model evaluation script ├── models │ └── power_consumption_model.pkl # Saved trained model ├── README.md # Project overview ├── requirements.txt # Required libraries └── LICENSE # Open-source license

---

## Steps to Run the Project

### 1. Install Required Libraries
Install the required Python libraries using the following command:
```bash
pip install -r requirements.txt
2. Data Exploration
Run the data_exploration.py script to explore the dataset and visualize the data:

3. Preprocess the Data
Run the preprocess.py script to preprocess the dataset:

4. Train the Model
Run the train_model.py script to train the Linear Regression model:

5. Evaluate the Model
Run the evaluate_model.py script to evaluate the trained model and visualize the predictions:

Tools & Libraries
Programming Language: Python
Libraries:
pandas: For data manipulation and analysis.
matplotlib: For data visualization.
scikit-learn: For machine learning model training and evaluation.
joblib: For saving and loading the trained model.
Results
Model: Linear Regression
Performance Metric: Mean Squared Error (MSE)
Visualization: The plot below shows the comparison between actual and predicted power consumption for Zone 1.
Challenges & Learnings
Challenges:
Handling missing values in the dataset.
Ensuring the datetime format matched the dataset during preprocessing.
Normalizing the data for better model performance.
Learnings:
Gained experience in preprocessing time-series data.
Learned how to train and evaluate a regression model for forecasting.
Understood the importance of feature scaling in machine learning.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Name: Bhavya Patel
Email: pbhavya0826@gmail.com
