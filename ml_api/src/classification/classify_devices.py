import numpy as np

from app.tasks.load_models import models
from app.models.models import (
    ClassifiedDevices, 
    DeviceClassificationRequest, 
    DeviceClassificationResponse, 
    PeakOutput
)

device_mapping = {
    "washing_machine": 0,
    "dishwasher": 1,
    "dryer": 2,
    "freezer": 3,
    "fridge": 4,
    "micro_wave_oven": 5,
    "coffee": 6
}
device_mapping_inverse = {v: k for k, v in device_mapping.items()}

def preprocess_electricity_data(electricity_data):
    # Extract the power values from ElectricityInput
    power_values = [entry.power for entry in electricity_data]
    # Convert the list into a numpy array that model can handle inputs
    time_series_array = np.expand_dims(np.array(power_values), axis=-1)
    return time_series_array

def predict(electricity_consumption: DeviceClassificationRequest) -> DeviceClassificationResponse:
    results = []
    model = models["device_classification"]
    for peaks in electricity_consumption.peaks:
        time_series_padded = preprocess_electricity_data(peaks.electricity)
        predicted_probabilities = model.predict(np.array([time_series_padded]))
        classified_devices = []
        for i, prob in enumerate(predicted_probabilities[0]):
            device_name = device_mapping_inverse.get(i, f"Unknown Device {i}")
            classified_devices.append(ClassifiedDevices(name=device_name, confidence=float(prob)))
        results.append(PeakOutput(peak_id=peaks.peak_id, devices=classified_devices))
    return DeviceClassificationResponse(peaks=results)
