from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_session
from app.schemas.shipment_schemas import ShipmentCreate, ShipmentUpdate

router = APIRouter(prefix="shipments/", tags=["Shipments"])


@router.get("/retrieve_shipments")
def retrieve_shipments(db: AsyncSession = Depends(get_session())):
    return

@router.post("add_shipment")
def add_shipment(db: AsyncSession, shipment: ShipmentCreate):
    return

@router.put("/update_shipment")
def update_shipment(db: AsyncSession, shipment: ShipmentUpdate):
    return

@router.delete("/delete_shipment")
def delete_shipment(db: AsyncSession, shipment: ShipmentCreate):
    return