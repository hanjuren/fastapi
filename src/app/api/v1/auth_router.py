from fastapi import APIRouter
from loguru import logger

from app.common.aop.logging_api_route import LoggingAPIRoute

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    route_class=LoggingAPIRoute
)

@router.post("/sign-up")
async def sign_up():
    """
    create users record
    """
    logger.info("this is sign-up api.")
    return {
        "success": True
    }