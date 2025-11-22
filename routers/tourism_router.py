from fastapi import APIRouter
import pandas as pd

router = APIRouter(prefix="/api/tourism")

@router.get("/chengdu")
def get_chengdu_tourism():
    df = pd.read_csv("data/raw/chengdu_tourism.csv")
    return df.to_dict("records")