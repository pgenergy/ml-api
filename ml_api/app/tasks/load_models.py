import pickle as pkl

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

    with open(f"{model_path}svm_electricity_device_classifier.pkl", "rb") as f:
        default_values = pkl.load(f)  # nosec
        models["device_classification"] = default_values

    return models


models = load_models()
