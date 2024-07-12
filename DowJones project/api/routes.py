from fastapi import APIRouter, HTTPException, status, Depends
from typing import List, Optional
from models import PredictionRequest
import pandas as pd
from sklearn.metrics import mean_squared_error
import joblib
from prepro import load_data, preprocess_data
from datetime import datetime, timedelta
from enum import Enum
import os
from pydantic import BaseModel
from typing import Annotated, Union
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

fake_users_db = {
    "thomas": {
        "username": "thomas",
        "full_name": "tho mas",
        "email": "thomas@example.com",
        "hashed_password": "fakehashedtoto",
        "disabled": False,
    },
    "richard": {
        "username": "richard",
        "full_name": "ri chard",
        "email": "richard@example.com",
        "hashed_password": "fakehashedrichard",
        "disabled": False,
    },
    "sebastien": {
        "username": "sebastien",
        "full_name": "seb astien",
        "email": "sebastien@example.com",
        "hashed_password": "fakehashedsebastien",
        "disabled": False,
    },
}


def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user


@router.get("/")
def root(current_user: Annotated[User, Depends(get_current_active_user)]):
    return {"message": "API en ligne!"}


path_to_model_directory = os.path.join(os.path.dirname(__file__), "trainedModel")


def get_latest_model_path(directory):
    files = [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]
    return max(files, key=os.path.getctime)


latest_model_filename = get_latest_model_path(path_to_model_directory)
best_model = joblib.load(latest_model_filename)


@router.post("/predict/")
async def predict(
    request: PredictionRequest,
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    print("Fonction predict appelée")
    df = load_data(request.ticker)
    train_X, train_y, test_X, test_y, sc = preprocess_data(df)

    if request.days > len(test_X):
        raise HTTPException(
            status_code=400,
            detail="Le nombre de jours demandés dépassent les données de test disponibles",
        )
    features = test_X[: request.days]
    pred = best_model.predict(features)
    predictions = sc.inverse_transform(pred.reshape(-1, 1))
    actual_values = sc.inverse_transform(test_y[: request.days])
    mse = mean_squared_error(actual_values, predictions)
    print(type(predictions.tolist()))
    print(type(mse))
    current_dir = (
        os.getcwd()
    )  # added to try to understand why mse_records.csv is not found
    print(
        "Current working directory:", current_dir
    )  # added to try to understand why mse_records.csv is not found
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mse_data = pd.DataFrame(
        [[current_time, request.ticker, request.days, mse]],
        columns=["Time", "Ticker", "Days", "MSE"],
    )
    mse_data.to_csv("mse_records.csv", mode="a", header=False, index=False)

    return {"predictions": predictions.tolist(), "mse": mse}
