from typing import Dict, List
import numpy as np
import pandas as pd

from app.tasks.load_models import models
from app.models.models import DeviceClassificationResponse, DeviceClassificationRequest, ElectricityOutput


def predict(electricity_consumption: DeviceClassificationRequest) -> Dict:

    model = models["device_classification"]

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

        reading = reading.drop(labels=['Timestamp']).to_frame().T

        predictions_prob = model.predict_proba(reading)

        for i, probs in enumerate(predictions_prob):
            max_prob = max(probs) 
            predicted_class = model.classes_[probs.argmax()] 
            print("Vorhersage für Zeitpunkt {}: {} mit Genauigkeit {:.2f}%".format(i+1, predicted_class, max_prob*100))
            classification = predicted_class
        
        result[key] = ElectricityOutput(
            timestamp=value.timestamp,
            power=value.power,
            classification=classification
        )

    return result
