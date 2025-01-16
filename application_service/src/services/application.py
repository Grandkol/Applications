from schemas import ApplicationToBD
from models import Application
from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from schemas import ApplicationInBd


async def _create_application(
        session: AsyncSession,
        application: ApplicationToBD
):
    data = jsonable_encoder(application)
    app = Application(**data)
    session.add(app)
    await session.commit()
    await session.refresh(app)
    return app


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
