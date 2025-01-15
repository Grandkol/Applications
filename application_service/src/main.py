from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from fastapi.responses import ORJSONResponse

from api.v1 import applications
from core import settings


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield


app = FastAPI(
    title=settings.project_name,
    docs_url = "/app/openapi",
    openapi_url = "/app/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.include_router(applications.router, prefix="/app/v1", tags=["applications"])