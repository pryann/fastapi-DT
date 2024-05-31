import time
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi import FastAPI
from src.config import get_settings

settings = get_settings()


def setup_cors_middleware(app: FastAPI):
    cors_config = {
        "allow_origins": settings.CORS_ORINGINS_LIST,
        "allow_credentials": True,
        "allow_methods": ["*"],
        "allow_headers": ["*"],
    }
    # register a class
    app.add_middleware(CORSMiddleware, **cors_config)


# register a function
def setup_process_time_middleware(app: FastAPI):
    @app.middleware("http")
    async def add_process_time_header(request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response


def register_middlewares(app: FastAPI):
    setup_cors_middleware(app)
    setup_process_time_middleware(app)
    # if you do not need any config, etc.
    app.add_middleware(GZipMiddleware)
    # alternate solution for CORS
    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=settings.CORS_ORINGINS_LIST,
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )
