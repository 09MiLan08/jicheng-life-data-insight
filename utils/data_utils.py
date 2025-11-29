import pandas as pd
import os

# 获取CSV文件的绝对路径（适配不同系统）
def get_csv_path(filename):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "raw", filename)

# 读取美食数据
def read_food_data():
    df = pd.read_csv(get_csv_path("chengdu_food.csv"), encoding="utf-8")
    return df.to_dict("records")  # 转为字典列表，方便JSON返回

# 读取旅游景点数据
def read_tourism_data():
    df = pd.read_csv(get_csv_path("chengdu_tourism.csv"), encoding="utf-8")
    return df.to_dict("records")

# 读取交通数据
def read_traffic_data():
    df = pd.read_csv(get_csv_path("chengdu_traffic.csv"), encoding="utf-8")
    return df.to_dict("records")

# 读取公共服务数据
def read_public_service_data():
    df = pd.read_csv(get_csv_path("chengdu_public_service.csv"), encoding="utf-8")
    return df.to_dict("records")

# 读取消费活力数据
def read_consumption_data():
    df = pd.read_csv(get_csv_path("chengdu_consumption.csv"), encoding="utf-8")
    return df.to_dict("records")

# 读取生态宜居数据
def read_ecology_data():
    df = pd.read_csv(get_csv_path("chengdu_ecology.csv"), encoding="utf-8")
    return df.to_dict("records")

# 读取社区生活数据
def read_community_data():
    df = pd.read_csv(get_csv_path("chengdu_community.csv"), encoding="utf-8")
    return df.to_dict("records")