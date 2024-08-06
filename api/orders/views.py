from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.orders.schemas import OrderCreate
from api.orders import crud
from app.database import session_helper

router = APIRouter(tags=["Orders"], prefix="/api/v1/orders")


@router.get("/")
async def get_orders(
        target_date: datetime,
        session: AsyncSession = Depends(session_helper.scoped_session_dependency)
):
    orders = await crud.get_orders(session, target_date)
    return {
        "status": 200,
        "body": {"orders": orders}
    }


@router.post("/")
async def create_order(
        order: OrderCreate,
        session: AsyncSession = Depends(session_helper.scoped_session_dependency)
):
    order = await crud.create_order(session, order)
    if not order:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Couldn't find time for a walk")

    return {
        "status": 200,
        "body": {"order": order}
    }
