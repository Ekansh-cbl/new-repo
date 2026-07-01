from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from data import AppState
from routes import router


def create_app() -> FastAPI:
    app = FastAPI(title="DualCam Ops", version="1.0.0")
    app.state.store = AppState.sample()
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    app.state.templates = Jinja2Templates(directory="app/templates")
    app.include_router(router)
    return app
