from fastapi import APIRouter
import pandas as pd

# 接口前缀：/api/food，后续访问接口需加这个前缀
router = APIRouter(prefix="/api/food")

# 接口：获取成都美食数据（GET请求）
@router.get("/chengdu")
def get_chengdu_food():
    # 读取CSV数据（用你熟悉的pandas）
    df = pd.read_csv("data/raw/chengdu_food.csv")
    # 转换为字典格式，方便前端ECharts解析
    return df.to_dict("records")