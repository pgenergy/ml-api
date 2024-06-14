import pandas as pd

from app.tasks.load_models import models
from app.models.models import DeviceClassificationRequest, DeviceClassificationResponse, ElectricityOutput
from collections import defaultdict


def predict(electricity_consumption: DeviceClassificationRequest) -> DeviceClassificationResponse:

    model = models["device_classification"]
    results = []

    for consumption in electricity_consumption.electricity:

        reading = pd.Series({
            'Timestamp': consumption.timestamp,
        })

        reading["Year"] = pd.to_datetime(reading['Timestamp']).year
        reading["Month"] = pd.to_datetime(reading['Timestamp']).month
        reading["Date"] = pd.to_datetime(reading['Timestamp']).day
        reading["Hour"] = pd.to_datetime(reading['Timestamp']).hour
        reading["Minute"] = pd.to_datetime(reading['Timestamp']).minute
        reading["Second"] = pd.to_datetime(reading['Timestamp']).second
        reading["power"] = consumption.power

        reading = reading.drop(labels=['Timestamp']).to_frame().T

        predictions_prob = model.predict_proba(reading)

        class_probabilities = defaultdict(float)
        for i, probs in enumerate(predictions_prob):
            for j, prob in enumerate(probs):
                class_probabilities[model.classes_[j]] = round(prob * 100, 2)

        electricity = ElectricityOutput(
            timestamp=consumption.timestamp,
            power=consumption.power,
            dominant_classification=max(class_probabilities, key=class_probabilities.get),
            classification=class_probabilities
        )
        results.append(electricity)

    return DeviceClassificationResponse(electricity=results)
