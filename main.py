from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from datetime import timedelta
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from utils.data_utils import (
    read_food_data, read_tourism_data, read_traffic_data,
    read_public_service_data, read_consumption_data,
    read_ecology_data, read_community_data
)
import os


def read_food_data():

    return {
        # 柱状图：各区店铺数量
        "countLabels": ["锦江区", "武侯区", "青羊区", "成华区", "金牛区", "高新区", "天府新区"],
        "countValues": [77, 93, 73, 58, 53, 18, 16],  
        
        # 饼图：美食类型占比
        "typeData": [
            {"value": 117, "name": "川味正餐"},
            {"value": 153, "name": "川味小吃"},
            {"value": 92, "name": "本地特色"}
        ],
        
        # 散点图：评分与消费关系
        "scatterData": [
            {"name": "火锅", "value": [128, 4.8]},
            {"name": "串串香", "value": [86, 4.7]},
            {"name": "麻辣烫", "value": [65, 4.5]},
            {"name": "蛋烘糕", "value": [12, 4.6]},
            {"name": "钟水饺", "value": [28, 4.4]},
            {"name": "夫妻肺片", "value": [98, 4.9]},
            {"name": "龙抄手", "value": [32, 4.3]},
            {"name": "麻婆豆腐", "value": [75, 4.7]},
            {"name": "冰粉", "value": [15, 4.5]},
            {"name": "兔头", "value": [45, 4.8]}
        ]
    }

def read_tourism_data():
    return {
        # 折线图：客流量数据
        "flowLabels": ["大熊猫基地", "宽窄巷子", "锦里古街", "都江堰", "青城山", "春熙路", "杜甫草堂", "武侯祠", "东郊记忆", "文殊院"],
        "flowValues": [180, 150, 120, 110, 95, 365, 65, 85, 78, 45],
        
        # 饼图：类型占比数据
        "typeData": [
            {"value": 3, "name": "历史古迹"},
            {"value": 3, "name": "自然景观"},
            {"value": 2, "name": "民俗风情"},
            {"value": 1, "name": "商业旅游"},
            {"value": 1, "name": "文创旅游"}
        ],
        
        # 柱状图：门票价格数据
        "ticketLabels": ["武侯祠", "杜甫草堂", "大熊猫基地", "都江堰", "青城山"],
        "ticketValues": [50, 50, 55, 80, 90]
    }

def read_traffic_data():

    return {
        # 柱状图：地铁线路运营里程
        "mileageLabels": ["1号线", "2号线", "3号线", "4号线", "5号线", "7号线", "10号线"],
        "mileageValues": [41.0, 42.3, 49.9, 38.9, 49.0, 38.6, 37.9],  # 对应各线路里程（公里）
        
        # 折线图：早晚高峰客流
        "flowLabels": ["1号线", "2号线", "3号线", "4号线", "5号线", "7号线", "10号线"],  
        "morningPeakValues": [35.2, 31.5, 28.7, 25.1, 26.8, 22.3, 18.5],  
        "eveningPeakValues": [32.8, 29.6, 27.3, 23.9, 25.5, 21.7, 17.2],  
        
        # 饼图：出行方式占比
        "modeData": [
            {"value": 210, "name": "地铁"},
            {"value": 85, "name": "公交"},
            {"value": 10, "name": "航空"},
            {"value": 150, "name": "私家车"}
        ]
    }

def read_public_service_data():

    return {
        # 柱状图：各区三甲医院数量
        "hospitalLabels": ["锦江区", "武侯区", "青羊区", "成华区", "金牛区", "高新区", "天府新区"],
        "hospitalValues": [6, 8, 7, 5, 6, 4, 3],  
        
        # 堆叠柱状图：中小学+幼儿园数量
        "schoolLabels": ["锦江区", "武侯区", "青羊区", "成华区", "金牛区", "高新区", "天府新区"],  
        "primarySecondaryValues": [32, 41, 35, 30, 33, 28, 25],  
        "kindergartenValues": [45, 53, 48, 42, 46, 40, 38],  
        
        # 饼图：人才类型占比
        "talentData": [
            {"value": 363.8, "name": "专业技术人才"},
            {"value": 313.1, "name": "技能人才"}
        ]
    }

def read_consumption_data():

    return {
        # 柱状图：各业态首店数量
        "storeLabels": ["餐饮", "零售", "潮玩", "美妆", "亲子", "运动", "文创"],
        "storeValues": [320, 285, 98, 126, 89, 112, 76], 
        
        # 横向柱状图：主要商圈日均客流量
        "businessLabels": ["春熙路", "太古里", "IFS", "宽窄巷子", "万象城", "环球中心", "大悦城"],  
        "businessValues": [50.2, 42.8, 28.5, 35.6, 25.3, 22.7, 19.8],  
        
        # 饼图：社会消费品零售额占比
        "salesData": [
            {"value": 186.5, "name": "餐饮"},
            {"value": 215.3, "name": "零售"},
            {"value": 68.7, "name": "潮玩"},
            {"value": 92.4, "name": "美妆"},
            {"value": 75.2, "name": "亲子"},
            {"value": 83.6, "name": "运动"},
            {"value": 52.8, "name": "文创"}
        ]
    }

def read_ecology_data():

    return {
        # 柱状图：各区天府绿道长度
        "greenwayLabels": ["锦江区", "武侯区", "青羊区", "成华区", "金牛区", "高新区", "天府新区"],
        "greenwayValues": [85.2, 92.7, 78.5, 88.3, 75.6, 120.8, 156.3], 
        
        # 折线图：各区建成区绿化覆盖率
        "coverageLabels": ["锦江区", "武侯区", "青羊区", "成华区", "金牛区", "高新区", "天府新区"], 
        "coverageValues": [45.3, 46.1, 44.9, 43.7, 42.8, 48.2, 52.5],  
        
        # 饼图：生态区域面积占比
        "ecoAreaData": [
            {"value": 697.4, "name": "绿道"},
            {"value": 380.0, "name": "森林公园"},
            {"value": 15.0, "name": "大熊猫栖息地"},
            {"value": 210.0, "name": "城市公园"}
        ]
    }

def read_community_data():

    return {
        # 柱状图：各区养老综合体数量
        "elderlyLabels": ["锦江区", "武侯区", "青羊区", "成华区", "金牛区", "高新区", "天府新区"],
        "elderlyValues": [5, 6, 6, 4, 5, 3, 4],  
        
        # 堆叠柱状图：便利店+茶馆密度
        "storeDensityLabels": ["锦江区", "武侯区", "青羊区", "成华区", "金牛区", "高新区", "天府新区"],  
        "convenienceStoreValues": [3.2, 3.5, 3.0, 2.7, 2.9, 3.8, 3.1],  
        "teahouseValues": [2.8, 3.1, 3.3, 3.5, 3.2, 2.5, 2.7],  
        
        # 饼图：康养服务月均服务次数
        "healthData": [
            {"value": 8650, "name": "上门护理"},
            {"value": 6400, "name": "康复指导"}
        ]
    }


# 创建FastAPI应用实例
app = FastAPI(title="成都城市生活数据洞察平台", version="1.0")

# 挂载静态文件（让FastAPI能访问static目录下的HTML、JS、CSS）
app.mount("/static",StaticFiles(directory="static"),  name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 正式环境要写具体域名，比如["http://你的前端域名"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 设置模板目录（用于渲染index.html）
templates = Jinja2Templates(directory="static")

# 自定义文档路径（可选，默认是/docs）
@app.get("/docs", include_in_schema=False)
def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="成都数据平台接口文档",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url
    )

@app.get("/openapi.json", include_in_schema=False)
def get_open_api_endpoint():
    return get_openapi(title="成都数据平台接口文档", version="1.0.0", routes=app.routes)

# 首页路由：访问根路径，返回index.html
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 7大场景数据接口（每个接口返回对应CSV的JSON数据）
@app.get("/api/food", summary="美食数据接口")
async def get_food_data():
    return {"data": read_food_data()}

@app.get("/api/tourism", summary="旅游景点数据接口")
async def get_tourism_data():
    return {"data": read_tourism_data()}

@app.get("/api/traffic", summary="交通出行数据接口")
async def get_traffic_data():
    return {"data": read_traffic_data()}

@app.get("/api/public-service", summary="公共服务数据接口")
async def get_public_service_data():
    return {"data": read_public_service_data()}

@app.get("/api/consumption", summary="消费活力数据接口")
async def get_consumption_data():
    return {"data": read_consumption_data()}

@app.get("/api/ecology", summary="生态宜居数据接口")
async def get_ecology_data():
    return {"data": read_ecology_data()}

@app.get("/api/community", summary="社区生活数据接口")
async def get_community_data():
    return {"data": read_community_data()}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": "请求出错啦~请稍后再试"}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "服务器开小差了~"}
    )

# 运行说明：在终端执行 `uvicorn main:app --reload`，启动后访问 http://127.0.0.1:8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)