from typing import Dict
import numpy as np
import pandas as pd

from app.tasks.load_models import models
from app.models.models import DeviceClassificationRequest, ElectricityOutput


def predict(electricity_consumption: DeviceClassificationRequest) -> Dict:

    model = models["device_classification"]
    classification = ""
    result = {}

    for key, value in electricity_consumption.electricity.items():

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

        for probs in enumerate(predictions_prob):
            predicted_class = model.classes_[probs.argmax()] 
            classification = predicted_class
        
        result[key] = ElectricityOutput(
            timestamp=value.timestamp,
            power=value.power,
            classification=classification
        )

    return result
