from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles  # 挂载静态文件（HTML）
from routers import food_router  # 导入美食接口路由
from routers import tourism_router

# 初始化FastAPI应用
app = FastAPI()

# 挂载static目录，让浏览器能访问HTML文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 注册路由（让接口生效）
app.include_router(food_router.router)
app.include_router(tourism_router.router)

# 测试接口（可选，访问根路径时返回提示）
@app.get("/")
def root():
    return {"message": "FastAPI数据洞察平台启动成功！访问 /static/index.html 看可视化图表"}