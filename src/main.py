import uvicorn
from fastapi import FastAPI
from loguru import logger

from app.api.routers import v1
from app.common.conf.service_conf import settings
from app.common.logger.log import Logger


def create_app():
    Logger.make_logger()

    application = FastAPI(
        title='FastAPI Server',
        version='0.0.1',
        openapi_url="/swagger.json",
    )

    application.include_router(v1)

    return application

app = create_app()

if __name__ == '__main__':
    try:
        logger.info(
                """\n
/$$$$$$$$                   /$$      /$$$$$$  /$$$$$$$  /$$$$$$
| $$_____/                  | $$     /$$__  $$| $$__  $$|_  $$_/
| $$    /$$$$$$   /$$$$$$$ /$$$$$$  | $$  | $$| $$  | $$  | $$
| $$$$$|____  $$ /$$_____/|_  $$_/  | $$$$$$$$| $$$$$$$/  | $$
| $$__/ /$$$$$$$|  $$$$$$   | $$    | $$__  $$| $$____/   | $$
| $$   /$$__  $$ |____  $$  | $$ /$$| $$  | $$| $$        | $$
| $$  |  $$$$$$$ /$$$$$$$/  |  $$$$/| $$  | $$| $$       /$$$$$$
|__/   |_______/|_______/    |___/  |__/  |__/|__/      |______/
"""
        )
        uvicorn.run(
            app="main:app",
            host="0.0.0.0",
            port=settings.get('SERVICE_PORT', 8000),
            reload=settings.get('RELOAD', True),
        )
    except Exception as e:
        logger.error(f"❌ FastAPI start failed: {e}")


