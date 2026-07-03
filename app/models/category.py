from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    category_id = Column("CATEGORY_ID", Integer, primary_key=True, autoincrement=True)
    user_id = Column("USER_ID", Integer, ForeignKey("users.USER_ID"), nullable=False)
    category_name = Column("CATEGORY_NAME", String(50), nullable=False)
