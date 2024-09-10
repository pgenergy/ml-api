from tensorflow.keras.models import load_model
from app.settings import settings
from os import path

import pandas as pd

def load_models():
    """
    load the models from disk
    and put them in a dictionary

    Returns:
        dict: loaded models
    """
    print("models loaded from disk")
    model_path = settings.models_path
    models = {}
    model_file = path.join(model_path, "appliance_classification_model-2024-08-27.keras")
    models["device_classification"] = load_model(model_file)
    models["co2prediction"] = pd.read_csv(path.join(model_path, "co2_regression.csv"))
    return models


models = load_models()
