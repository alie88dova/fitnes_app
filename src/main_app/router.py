from fastapi import APIRouter,  Request, Depends
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    tags=["/"]
)

@router.get("/")
def get_base_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})