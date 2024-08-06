from datetime import datetime
from typing import List, Optional

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Order, Walker
from api.orders.schemas import OrderCreate


async def create_order(session: AsyncSession, order: OrderCreate) -> Optional[Order]:
    existing_orders = await get_orders(session, order.walk_datetime)
    if len(existing_orders) == 2:
        return

    walk_datetime = order.walk_datetime
    order.walk_datetime = walk_datetime.replace(tzinfo=None)
    walker = Walker.Anton.name if len(existing_orders) == 0 else Walker.Petr.name
    order = Order(**order.dict(), walker=walker)
    session.add(order)

    await session.commit()
    await session.refresh(order)

    return order


async def get_orders(session: AsyncSession, target_datetime: datetime) -> List[Order]:
    target_datetime = target_datetime.replace(tzinfo=None)
    stmt = (select(Order)
            .where(Order.walk_datetime == target_datetime)
            .order_by(Order.id))

    result: Result = await session.execute(stmt)
    orders = result.scalars().all()
    return list(orders)
