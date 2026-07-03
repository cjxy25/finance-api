from fastapi import FastAPI
from app.routers import auth, bill, category

app = FastAPI(title="个人财务管理 API", version="0.1.0")
app.include_router(auth.router)
app.include_router(bill.router)
app.include_router(category.router)

@app.get("/")
def root():
    return {"message": "财务管理 API 运行中"}
