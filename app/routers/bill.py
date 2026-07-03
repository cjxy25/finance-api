from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import extract
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.database import get_db
from app.models.bill import Bill
from app.models.category import Category

router = APIRouter()


# ── 创建账单 ──────────────────────────────────

class CreateBillRequest(BaseModel):
    money: float
    place: str
    bill_time: datetime
    category_id: int
    remark: str


@router.post("/bills")
def create_bill(req: CreateBillRequest, db: Session = Depends(get_db)):
    new_bill = Bill(
        bill_time=req.bill_time,
        place=req.place,
        money=req.money,
        user_id=1,
        category_id=req.category_id,
        remark=req.remark
    )
    db.add(new_bill)
    db.commit()
    return {"msg": "创建成功"}


# ── 查询账单列表 ──────────────────────────────

@router.get("/bills")
def list_bills(
    db: Session = Depends(get_db),
    year: Optional[int] = None,
    month: Optional[int] = None,
    day: Optional[int] = None,
    amount_op: Optional[str] = None,
    amount_value: Optional[float] = None,
    category_id: Optional[int] = None,
):
    filters = []

    # 时间筛选
    if year:
        filters.append(extract("year", Bill.bill_time) == year)
    if month is not None:
        if month < 1 or month > 12:
            return {"error": "月份无效"}
        filters.append(extract("month", Bill.bill_time) == month)
    if day is not None:
        if day < 1 or day > 31:
            return {"error": "日期无效"}
        filters.append(extract("day", Bill.bill_time) == day)

    # 金额筛选
    if amount_op and amount_value is not None:
        if amount_op == ">":
            filters.append(Bill.money > amount_value)
        elif amount_op == "<":
            filters.append(Bill.money < amount_value)
        else:
            return {"error": "操作符只能是 > < "}

    # 分类筛选
    if category_id:
        filters.append(Bill.category_id == category_id)

    bills = db.query(Bill).filter(*filters).all()
    total = sum(bill.money for bill in bills)
    return {
        "total": total,
        "bills": bills
    }
# ── 删除账单 ──────────────────────────────

@router.delete("/bills/{bill_id}")
def delete_bill(bill_id: int, db: Session = Depends(get_db)):
    bill = db.query(Bill).filter(Bill.bill_id == bill_id).first()
    if not bill:
        return {"error": "账单不存在"}
    db.delete(bill)
    db.commit()
    return {"msg": "删除成功"}