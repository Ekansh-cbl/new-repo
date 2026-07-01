from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


def render(request: Request, template_name: str, **context):
    templates = request.app.state.templates
    return templates.TemplateResponse(template_name, {"request": request, **context})


@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return render(request, "dashboard.html", store=request.app.state.store)


@router.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return render(request, "register.html", store=request.app.state.store, success=False)


@router.post("/register")
def submit_registration(
    request: Request,
    full_name: str = Form(...),
    notes: str = Form(""),
    camera: str = Form("Inbuilt Camera"),
):
    store = request.app.state.store
    store.capture_progress = min(store.capture_target, store.capture_progress + 1)
    return render(
        request,
        "register.html",
        store=store,
        success=True,
        submitted_name=full_name,
        submitted_camera=camera,
        submitted_notes=notes,
    )


@router.get("/people", response_class=HTMLResponse)
def people(request: Request):
    return render(request, "people.html", store=request.app.state.store)


@router.get("/training", response_class=HTMLResponse)
def training(request: Request):
    return render(request, "training.html", store=request.app.state.store)


@router.get("/health")
def health():
    return {"status": "ok"}
