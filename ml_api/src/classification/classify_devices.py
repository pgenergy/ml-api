from typing import Dict, List
import numpy as np
import pandas as pd

from app.tasks.load_models import models
from app.models.models import DeviceClassificationResponse, DeviceClassificationRequest, ElectricityOutput

def predict(electricity_consumption: DeviceClassificationRequest) -> Dict:

    new_data = pd.DataFrame({
        'Timestamp': ['2024-04-17 08:00:00', '2024-04-17 09:00:00', '2024-04-17 10:00:00', '2022-01-10 05:05:05'],
        'Year': [2024, 2024, 2024, 2024],
        'Month': [4, 4, 4, 1],
        'Date': [17, 17, 17, 10],
        'Hour': [8, 9, 10, 5],
        'Minute': [0, 0, 0, 5],
        'Second': [0, 0, 0, 5],
        'power': [0.5, 1.2, 10.8, 5.0]
    })

    new_data['Year'] = pd.to_datetime(new_data['Timestamp']).dt.year
    new_data['Month'] = pd.to_datetime(new_data['Timestamp']).dt.month
    new_data['Date'] = pd.to_datetime(new_data['Timestamp']).dt.day
    new_data['Hour'] = pd.to_datetime(new_data['Timestamp']).dt.hour
    new_data['Minute'] = pd.to_datetime(new_data['Timestamp']).dt.minute
    new_data['Second'] = pd.to_datetime(new_data['Timestamp']).dt.second

    new_data.drop(columns=['Timestamp'], inplace=True)

    model = models["device_classification"]

    predictions_prob = model.predict_proba(new_data)

    print("Test in predict")

    classification = ""

    result = {}

    print(electricity_consumption)

    for key, value in electricity_consumption.electricity.items():
        
        print(value.timestamp)
        print(type(pd.to_datetime(value.timestamp)))

        reading = pd.Series({
            'Timestamp': value.timestamp,
        })

        reading["Year"] = pd.to_datetime(reading['Timestamp']).year
        reading["Month"] = pd.to_datetime(reading['Timestamp']).month
        reading["Date"] = pd.to_datetime(reading['Timestamp']).day
        reading["Hour"] = pd.to_datetime(reading['Timestamp']).hour
        reading["Minute"] = pd.to_datetime(reading['Timestamp']).minute
        reading["Second"] = pd.to_datetime(reading['Timestamp']).second
        reading["power"] = value.power

        #reading.drop(columns=['Timestamp'], inplace=True)
        reading = reading.drop(labels=['Timestamp'])

        print(reading)

        reading = reading.to_frame().T

        print(reading)

        predictions_prob = model.predict_proba(reading)

        for i, probs in enumerate(predictions_prob):
            max_prob = max(probs) 
            predicted_class = model.classes_[probs.argmax()] 
            print("Vorhersage für Zeitpunkt {}: {} mit Genauigkeit {:.2f}%".format(i+1, predicted_class, max_prob*100))
            print(new_data['Year'][i])
            classification = predicted_class
        
        result[key] = ElectricityOutput(
            timestamp=value.timestamp,
            power=value.power,
            classification=classification
        )

    return result