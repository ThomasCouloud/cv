import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os


def load_data(ticker: str):

    if os.environ.get("RUNNING_IN_DOCKER") == "True":
        csv_path = "/model_training/data/OPA.csv"
    else:
        csv_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "LoadData/data/OPA.csv"
        )

    df = pd.read_csv(csv_path, parse_dates=[0], header=[0, 1], index_col=0)
    df = df.xs(ticker, level=1, axis=1)
    df["Mean"] = (df["Low"] + df["High"]) / 2
    return df


def preprocess_data(df: pd.DataFrame):
    df["Actual"] = df["Adj Close"].shift(-1)
    df = df.dropna()

    cols_to_scale = [
        "Adj Close",
        "Close",
        "High",
        "Low",
        "Open",
        "Volume",
        "Google Trends",
        "Mean",
    ]

    sc = MinMaxScaler(feature_range=(0, 1))
    X = sc.fit_transform(df[cols_to_scale])
    y = sc.fit_transform(df[["Actual"]])

    train_size = int(len(df) * 0.9)
    train_X, test_X = X[:train_size], X[train_size:]
    train_y, test_y = y[:train_size], y[train_size:]

    return train_X, train_y, test_X, test_y, sc
