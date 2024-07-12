from typing import List
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    ticker: str
    days: int
