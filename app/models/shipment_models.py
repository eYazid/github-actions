from datetime import datetime
from enum import Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float, DateTime, CheckConstraint, Enum as SEnum


class Base(DeclarativeBase):
    pass


class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


class Shipment(Base):
    __tablename__ = "shipment"
    __table_args__ = (CheckConstraint("weight <= 25", name="check_employee_age"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String(100))
    weight: Mapped[float] = mapped_column(Float, primary_key=True)
    destination: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[ShipmentStatus] = mapped_column(
        SEnum(ShipmentStatus), nullable=False, default=ShipmentStatus.placed
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now
    )
    estimated_delivery: Mapped[datetime]
