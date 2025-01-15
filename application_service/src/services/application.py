from schemas import ApplicationToBD
from models import Application
from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession

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
