import http

from schemas import ApplicationToBD
from models import Application
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from rest_framework import status

from schemas import ApplicationInBd

from core import logger


async def _create_application(
        session: AsyncSession,
        application: ApplicationToBD
):
    msg = 'Пустая заявка не может быть обработана'
    try:
        data = jsonable_encoder(application)
        app = Application(**data)
        session.add(app)
        await session.commit()
        await session.refresh(app)
        return app
    except:
        logger.info('A Null object was transferred to the database.')
        raise HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED,
            detail="You had already logged out.",
        )


async def _get_applications(
    session: AsyncSession,
    user_name,
):
    app = await session.execute(select(Application))
    if user_name:
        app = await session.execute(
            select(Application).where(Application.user_name == user_name)
        )

    app = app.scalars().all()

    return [ApplicationInBd(**i.__dict__) for i in app]
