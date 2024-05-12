from typing import Dict, List
import numpy as np
import pandas as pd

from app.tasks.load_models import models

#def predict(electricity_consumption: dict) -> Dict:
def predict() -> Dict:

    test = {}

    new_data = pd.DataFrame({
        'Timestamp': ['2024-04-17 08:00:00', '2024-04-17 09:00:00', '2024-04-17 10:00:00', '2022-01-10 05:05:05'],
        'Year': [2024, 2024, 2024, 2024],
        'Month': [4, 4, 4, 1],
        'Date': [17, 17, 17, 10],
        'Hour': [8, 9, 10, 5],
        'Minute': [0, 0, 0, 5],
        'Second': [0, 0, 0, 5],
        'power': [0.5, 1.2, 10.8, 5.0]  # Beispielwerte für den Stromverbrauch
    })

    # Extrahiere die erforderlichen Merkmale aus der Timestamp-Spalte von new_data
    new_data['Year'] = pd.to_datetime(new_data['Timestamp']).dt.year
    new_data['Month'] = pd.to_datetime(new_data['Timestamp']).dt.month
    new_data['Date'] = pd.to_datetime(new_data['Timestamp']).dt.day
    new_data['Hour'] = pd.to_datetime(new_data['Timestamp']).dt.hour
    new_data['Minute'] = pd.to_datetime(new_data['Timestamp']).dt.minute
    new_data['Second'] = pd.to_datetime(new_data['Timestamp']).dt.second

    # Entferne die Timestamp-Spalte, da sie nicht mehr benötigt wird
    new_data.drop(columns=['Timestamp'], inplace=True)

    model = models["device_classification"]

    predictions_prob = model.predict_proba(new_data)

    print("Test in predict")

    for i, probs in enumerate(predictions_prob):
        max_prob = max(probs)  # Höchste Wahrscheinlichkeit für diese Vorhersage
        predicted_class = model.classes_[probs.argmax()]  # Vorhergesagte Klasse mit höchster Wahrscheinlichkeit
        print("Vorhersage für Zeitpunkt {}: {} mit Genauigkeit {:.2f}%".format(i+1, predicted_class, max_prob*100))
        print(new_data['Year'][i])

    return test