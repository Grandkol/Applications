from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request
from schemas import ApplicationToBD, ApplicationInBd
from sqlalchemy.ext.asyncio import AsyncSession
from db import db_helper
from services.application import _create_application

router = APIRouter()


@router.post('/applications',response_model=ApplicationInBd, status_code=HTTPStatus.CREATED)
async def create_application(
        application: ApplicationToBD,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    app = await _create_application(session=session, application=application)
    return app