from fastapi import APIRouter

from app.api.v1.auth_router import router as auth_router
from app.common.aop.logging_api_route import LoggingAPIRoute

v1 = APIRouter(prefix="/api/v1")

v1.include_router(auth_router)

# health check
@v1.get(
    "/health",
    name="Health Check API Server",
    description="server health check api",
    include_in_schema=False,
)
async def health_check():
    return {}
