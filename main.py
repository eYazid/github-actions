from fastapi import FastAPI
from contextlib import asynccontextmanager
from scalar_fastapi import get_scalar_api_reference
from rich import print, panel

from database.session import create_db_tables, close_session


@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    print(panel.Panel("Server Starting ... ", border_style="green"))
    await create_db_tables()
    # TODO: insert test data
    yield
    await close_session()
    print(panel.Panel("Server Stopped ... ", border_style="red"))


app = FastAPI(lifespan=lifespan_handler)


@app.get("/health")
def get_shipment():
    return {"status": "alive"}


@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title=app.title)
