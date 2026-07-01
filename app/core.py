from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.data import AppState
from app.routes import router

BASE_DIR = Path(__file__).resolve().parent
APP_DIR = BASE_DIR / "app"


def create_app() -> FastAPI:
    app = FastAPI(title="DualCam Ops", version="1.0.0")
    app.state.store = AppState.sample()
    app.mount("/static", StaticFiles(directory=str(APP_DIR / "static")), name="static")
    app.state.templates = Jinja2Templates(directory=str(APP_DIR / "templates"))
    app.include_router(router)
    return app
