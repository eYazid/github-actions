from pydantic import BaseModel, Field
from enum import Enum


class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


class BaseShipments(BaseModel):
    content: str
    weight: float = Field(le=25)
    destination: int
    status: ShipmentStatus


class ShipmentRead(BaseShipments):
    status: ShipmentStatus
    events: list


class ShipmentCreate(BaseShipments):
    status: ShipmentStatus = Field(default=ShipmentStatus.placed)


class ShipmentUpdate(BaseModel):
    content: str | None = Field(default=None)
    weight: float | None = Field(le=25, default=None)
    destination: int | None = Field(default=None)
    status: ShipmentStatus


if __name__ == "__main__":
    print(ShipmentCreate(content="rfvf", weight=12, destination="12"))
