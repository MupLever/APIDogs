from typing import List
from datetime import datetime

from sqlalchemy import select, Result, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Order
from api.orders.schemas import OrderCreate


async def create_order(session: AsyncSession, order: OrderCreate) -> Order:
    order = Order(**order.dict())
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order


async def get_orders(session: AsyncSession, target_date: datetime) -> List[Order]:
    stmt = (select(Order)
            .where(func.date(Order.walk_date) == target_date)
            .order_by(Order.id))

    result: Result = await session.execute(stmt)
    orders = result.scalars().all()
    return list(orders)
