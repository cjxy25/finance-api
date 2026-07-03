"""User 模型"""

from sqlalchemy import Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column("USER_ID", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(50), nullable=False)
    password_hash = Column("PASSWORD_HASH", String(256), nullable=False)
