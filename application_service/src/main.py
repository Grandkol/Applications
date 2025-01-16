from contextlib import asynccontextmanager

from db import db_helper
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi_pagination import add_pagination

from api.v1 import applications
from core import settings


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield

    await db_helper.dispose()


app = FastAPI(
    title=settings.project_name,
    docs_url="/app/openapi",
    openapi_url="/app/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
add_pagination(app)

app.include_router(applications.router, prefix="/app/v1", tags=["applications"])
