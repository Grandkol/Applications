from collections.abc import AsyncGenerator

from core import settings
from models.base import Base
from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    async_sessionmaker, create_async_engine)


class DatabaseHelper:
    def __init__(
        self,
        host: str,
        port: int,
        name: str,
        user: str,
        password: str,
        echo: bool = True,
        echo_pool: bool = False,
        pool_size: int = 5,
        max_overflow: int = 10,
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}",
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )

        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper(
    host=settings.db.host,
    user=settings.db.user,
    port=settings.db.port,
    password=settings.db.password,
    name=settings.db.name,
    echo_pool=settings.db.echo_pool,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)