from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_session

router = APIRouter(prefix="shipments/", tags=["Shipments"])


@router.get("/retrieve_shipments")
def retrieve_shipments(db: AsyncSession = Depends(get_session())):
    return
