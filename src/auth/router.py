import random
import string

from fastapi import APIRouter, Depends, Request
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import auth_backend, fastapi_users, current_active_user
from auth.models import user
from auth.schemas import UserRead, UserCreate
from auth.utils import User
from starlette.templating import Jinja2Templates

from db import get_async_session

router = APIRouter(
    tags=["Auth"]
)


templates = Jinja2Templates(directory="templates")


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

@router.get("/auth/login")
async def get_login_page(request: Request):
    print(request)
    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
        }
    )


@router.get("/test_correct_connet")
async def protected_route(user: User = Depends(current_active_user)):

    return {
            "status": "success",
            "data": None,
            "details": None,
    }



@router.post("/create_special_key")
async def create_spesial_key(session: AsyncSession = Depends(get_async_session),l_user: User = Depends(current_active_user)):
    letters = string.ascii_letters
    rand_string = ''.join(random.choice(letters) for i in range(256))
    stmt = (
        update(user).
        where(user.c.email == l_user.email).
        values(special_key=f'{rand_string}')
    )
    await session.execute(stmt)
    await session.commit()
    return {
        "status": "success"
    }