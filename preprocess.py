import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Convert 'Datetime' to datetime object and set as index
    data['Datetime'] = pd.to_datetime(data['Datetime'], format='%m/%d/%Y %H:%M')  # Corrected format
    data.set_index('Datetime', inplace=True)

    # Fill missing values
    data.fillna(method='ffill', inplace=True)

    # Normalize the features
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)
    data = pd.DataFrame(scaled_data, columns=data.columns, index=data.index)

    return data