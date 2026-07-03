"""Bill 模型"""

from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey

from app.database import Base
from app.models.category import Category



class Bill(Base):
    __tablename__ = "bills"

    bill_id = Column("BILL_ID", Integer, primary_key=True, autoincrement=True)
    user_id = Column("USER_ID", Integer, ForeignKey("users.USER_ID"), nullable=False)
    bill_time = Column("BILL_TIME", DateTime, nullable=False)
    place = Column("PLACE", String(50), nullable=False)
    category_id = Column("CATEGORY_ID", Integer, ForeignKey("categories.CATEGORY_ID"), nullable=False)
    money = Column("MONEY", DECIMAL(10, 2), nullable=False)
    remark = Column("REMARK", String(256), nullable=True)
