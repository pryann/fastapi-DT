from fastapi import FastAPI
from src.exception_handlers import register_exception_handlers
from src.user import router as user_router
from src.auth import router as auth_router
from src.middlewares import register_middlewares

app = FastAPI(title="My Big Project", version="0.1")

app.include_router(user_router.router)
app.include_router(auth_router.router)
register_middlewares(app)
register_exception_handlers(app)
