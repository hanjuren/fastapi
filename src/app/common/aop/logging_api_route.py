import uuid
from typing import Callable, Dict, Any

from fastapi.routing import APIRoute
from loguru import logger
from starlette.requests import Request
from starlette.responses import Response


class LoggingAPIRoute(APIRoute):

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request_id = str(uuid.uuid4())
            request.state.request_id = request_id

            await self._request_log(request)
            response: Response = await original_route_handler(request)
            self._response_log(request, response)
            return response

        return custom_route_handler

    @staticmethod
    def _has_json_body(request: Request) -> bool:
        if request.method in ("POST", "PUT", "PATCH") and request.headers.get("content-type") == "application/json":
            return True
        return False

    async def _request_log(self, request: Request) -> None:
        extra: Dict[str, Any] = {
            "httpMethod": request.method,
            "url": request.url.path,
            "headers": request.headers,
            "queryParams": request.query_params,
            "request_id": request.state.request_id,
        }

        if self._has_json_body(request):
            request_body = await request.body()
            extra["body"] = request_body.decode("UTF-8")

        logger.info(
            f"[REQUEST]: request_id={request.state.request_id}, method={request.method}, url={request.url}\n"
            f"client={request.client}, headers={request.headers}"
        )

    @staticmethod
    def _response_log(request: Request, response: Response) -> None:
        logger.info(
            f"[RESPONSE]: request_id={request.state.request_id}, url={request.method} {request.url} {response.status_code}"
        )