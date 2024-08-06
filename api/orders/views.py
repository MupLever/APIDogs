from datetime import datetime, date

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.orders.schemas import OrderCreate
from api.orders.crud import get_orders, create_order
from app.database import session_helper

router = APIRouter(tags=["Orders"], prefix="/api/v1/orders")


@router.get("/")
async def get_orders(
        target_date: datetime,
        session: AsyncSession = Depends(session_helper.scoped_session_dependency)
):
    orders = await get_orders(session, target_date)
    return {
        "status": 200,
        "body": {"orders": orders}
    }


@router.post("/")
async def create_order(
        order: OrderCreate,
        session: AsyncSession = Depends(session_helper.scoped_session_dependency)
):
    order = await create_order(session, order)
    return {
        "status": 200,
        "body": {"order": order}
    }
