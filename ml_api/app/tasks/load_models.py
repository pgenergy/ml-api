
import numpy as np
import pickle as pkl
import pandas as pd
import os

def load_models():
    """
    load the models from disk
    and put them in a dictionary
    Returns:
        dict: loaded models
    """

    print("models loaded from disk")

    model_path = "./models/"
    models = {}
    
    with open(f"{model_path}svm_electricity_device_classifier.pkl", "rb") as f:
        default_values = pkl.load(f)  # nosec
        models["device_classification"] = default_values    

    print(models["device_classification"])

    return models

models = load_models()
