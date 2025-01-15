from http import HTTPStatus
from typing import Annotated
import json

from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException, Request, Query
from schemas import ApplicationToBD, ApplicationInBd
from sqlalchemy.ext.asyncio import AsyncSession
from db import db_helper, kafka_controller
from services.application import _create_application, _get_applications

from core import settings


router = APIRouter()


@router.post(
    "/applications", response_model=ApplicationInBd, status_code=HTTPStatus.CREATED
)
async def create_application(
    application: ApplicationToBD,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):

    app = await _create_application(session=session, application=application)

    response_model = jsonable_encoder(
        ApplicationInBd(
            id=app.id,
            user_name=app.user_name,
            description=app.description,
            created_at=app.created_at,
        )
    )

    await kafka_controller.kafka_create_topic(topic=settings.kafka_topic)
    await kafka_controller.kafka_send(
        topic=settings.kafka_topic,
        value=json.dumps(response_model).encode("utf-8"),
        key=settings.kafka_key,
    )
    return app


@router.get("/applications", status_code=HTTPStatus.OK)
async def create_application(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        user_name: Annotated[
            str | None, Query(description="Query to find user applications")
        ] = None,
        page_size: Annotated[
            int, Query(description="Amount of applications at single page", ge=1)
        ] = None,
        page_number: Annotated[int, Query(description="Page number", ge=1)] = None,
):
    app = await _get_applications(session=session,
                                  user_name=user_name,
                                  page_size=page_size,
                                  page_number=page_number)
    return app
