from fastapi import APIRouter, Security, Query

from typing import Annotated

from app.models.general import check_api_key, general_responses
from app.models.co2prediction import Models, Co2PredictionRequest, Co2PredictionResponse
from app.tasks.load_models import models

import pandas as pd
import numpy as np

router = APIRouter()

spring_autumn = [2, 3, 9, 10]
winter = [11, 12, 1]


def calculate_avg_prediction(row, prediction_model):
    timestamp = row["timestamp"]

    series = None
    if timestamp.month in winter:
        series = prediction_model["hi"]
    elif timestamp.month in spring_autumn:
        series = prediction_model["md"]
    elif 4 <= timestamp.month <= 8:
        series = prediction_model["lw"]
    x_values = series.index.values
    y_values = series.values

    time = timestamp.hour + timestamp.minute / 60
    y_interpolated = np.interp(time, x_values, y_values)
    return y_interpolated * row["value"]


@router.post("/co2prediction",
             response_model=Co2PredictionResponse,
             responses={**general_responses})
def co2prediction(
        body: Co2PredictionRequest,
        model: Annotated[Models, Query()] = Models.default,
        api_key: str = Security(check_api_key)):

    if model == Models.default:
        model = Models.historic_average

    if len(body.data) == 0:
        return {
            "used_model": model,
            "data": []
        }

    data = pd.DataFrame([res.model_dump() for res in body.data])
    data["timestamp"] = pd.to_datetime(data["timestamp"])

    if model == Models.historic_average:
        data["value"] = data.apply(lambda row: calculate_avg_prediction(row, models["co2prediction"]), axis="columns")

    return {
        "used_model": model,
        "data": data.to_dict("records")
    }
