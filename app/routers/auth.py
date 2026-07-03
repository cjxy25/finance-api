from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models.user import User
from app.utils.security import hash_password, verify_password, create_access_token

router = APIRouter()


# 定义请求体
class RegisterRequest(BaseModel):
    name: str
    password: str


class LoginRequest(BaseModel):
    name: str
    password: str


@router.post("/register")
def register(req: RegisterRequest, db: Session = Depends(get_db)):
    # 1. 检查用户名是否已存在
    user = db.query(User).filter(User.name == req.name).first()
    if user:
        return {"error": "用户已存在"}

    hashed_pw = hash_password(req.password)# 2. 密码哈希
    new_user=User(name=req.name,password_hash=hashed_pw)
    db.add(new_user)
    db.commit()# 3. 创建用户写入数据库
    return {"msg": "注册成功"}# 4. 返回成功
@router.post("/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
    # 1. 查用户
    user = db.query(User).filter(User.name == req.name).first()
    if not user:
        return {"error": "用户不存在"}
    
    # 2. 验证密码
    if not verify_password(req.password, user.password_hash):
        return {"error": "密码错误"}
    
    # 3. 签发 token
    token = create_access_token({"sub": user.name})
    return {"token": token}
