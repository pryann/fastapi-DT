from fastapi import FastAPI
from src.user import router as user_router

app = FastAPI(title="My Big Project", version="0.1")
app.include_router(user_router.router)
