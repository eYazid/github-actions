from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.models.shipment_models import Base

from app.database.config import DatabaseSettings

db_settings = DatabaseSettings()

engine = create_async_engine(
    url=db_settings.POSTGRES_URL,
    echo=True,
)


async def create_db_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session():
    async_session = async_sessionmaker(
        bind=engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        yield session


async def close_session():
    await engine.dispose()
