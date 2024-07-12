import sys

# sys.path.append("Project-root/api")
## changed the path to project root in a relative not to get broken post commit / merge
import os

path_to_api = os.path.join(os.path.dirname(os.path.dirname(__file__)), "api")
sys.path.append(path_to_api)
import pytest
import numpy as np
from api.prepro import load_data, preprocess_data
from api.model_training import train_and_save_model


def test_xgboost_model_training_and_prediction():
    ticker = "AAPL"
    data = load_data(ticker)

    train_X, train_y, _, _, _ = preprocess_data(data)

    best_params = {
        "nthread": [4],
        "objective": ["reg:squarederror"],
        "learning_rate": [0.03, 0.05, 0.07],
        "max_depth": [5, 6, 7],
        "min_child_weight": [4],
        "silent": [1],
        "subsample": [0.7],
        "colsample_bytree": [0.7],
        "n_estimators": [100, 500, 1000],
    }

    result = train_and_save_model(train_X, train_y, best_params)
    assert "best_params" in result
