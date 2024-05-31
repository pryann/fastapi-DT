from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.exceptions import NotFoundError, AlreadyExistsError, AuthencticationError, AuthorizationError


def generate_response(status_code: int, message: str):
    return JSONResponse(
        status_code=status_code,
        content={"message": message}
    )


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(NotFoundError)
    async def not_found_exception_handler(request, exc):
        return generate_response(404, str(exc))

    @app.exception_handler(AlreadyExistsError)
    async def already_exists_exception_handler(request, exc):
        return generate_response(409, str(exc))

    @app.exception_handler(AuthencticationError)
    async def authentication_exception_handler(rrequest, exc):
        return generate_response(401, str(exc))

    @app.exception_handler(AuthorizationError)
    async def authorization_exception_handler(request, exc):
        return generate_response(403, str(exc))

    @app.exception_handler(500)
    def internal_server_error_handler(request, exc):
        return generate_response(500, "Internal server error")
