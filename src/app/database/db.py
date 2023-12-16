import sys
from typing import Annotated

from fastapi import Depends
from loguru import logger
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.common.conf.service_conf import settings


def create_engine_and_session(url: str | URL):
    print(url)
    try:
        engine = create_async_engine(url, echo=True, future=True, pool_pre_ping=True)
        logger.info('✅ Database Connection success')
    except Exception as e:
        logger.error('❌ Database Connection Error', e)
        sys.exit()
    else:
        db_session = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
        return engine, db_session


pg_user = settings.get("PG_USER")
pg_password = settings.get("PG_PASSWORD")
pg_host = settings.get("PG_HOST")
pg_port = settings.get("PG_PORT")
pg_database = settings.get("PG_DATABASE")

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"

async_engine, async_db_session = create_engine_and_session(SQLALCHEMY_DATABASE_URL)

async def get_db() -> AsyncSession:
    session = async_db_session()
    try:
        yield session
    except Exception as se:
        logger.error(se)
        await session.rollback()
        raise se
    finally:
        await session.close()

CurrentSession = Annotated[AsyncSession, Depends(get_db)]
