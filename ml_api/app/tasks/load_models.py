from tensorflow.keras.models import load_model
from app.settings import settings


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
    model_file = f"{model_path}appliance_classification_model.keras"
    models["device_classification"] = load_model(model_file)
    return models


models = load_models()