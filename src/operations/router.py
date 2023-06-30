import time

from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import user, trainer
from auth.utils import User
from db import get_async_session

from operations.models import PersProgram
from operations.schemas import AddPersProgramm
from auth.base_config import current_active_user

router = APIRouter(
    prefix="/operation",
)

#TODO Добавить проверику special key

@router.post("/get_all/")
async def get_all_programs(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(PersProgram)
        result = await session.execute(query)
        rs = [dict(zip(result.keys(), res)) for res in result.all()]
        return {
            "status": "success",
            "data": rs,
            "details": None
        }
    except Exception as e:
        return HTTPException(status_code=500, detail={
            "status": "error",
            "data": "Can't connect to databases"
        })


@router.post("/add_pers_program")
async def create_pers_prog(setd: AddPersProgramm, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(PersProgram).values(**setd.dict())
        await session.execute(stmt)
        await session.commit()
        return HTTPException(status_code=400, detail={
            "status": "success",
            "data": None,
            "details": None,
        })
    except Exception as e:
        #TODO дописать систему логирования
        return HTTPException(status_code=500, detail= {
            "status": "Error",
            "data": f"{e}",
            "details": None,
        })


@router.post("/your_programs")
async def get_your_programs(l_user: User = Depends(current_active_user), session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(PersProgram, user.c.email).join(user, PersProgram.c.client_id == user.c.id).where(
            PersProgram.c.id == 4
        )
        print(query)
        res = await session.execute(query)
        print(res.all())
        return {}
    except Exception as e:
        print(e)
        return HTTPException(status_code=500, detail={
            "status": "Error",
            "data": f"{e}",
            "details": None,
        })


#Пометка для себя кэширование работате только для get запросов))

@router.get("/your_program/")
@cache(expire=60)
def get_program(
        id_program: int,
        l_user: User = Depends(current_active_user),
        session: AsyncSession = Depends(get_async_session),
):
    try:
        "Код получения из бд программы пользователя"
        time.sleep(2)
        return {
            "status": "success",
            "data": {"name": "Имя программы", "text": "Какой-то текст из файла"},
            "details": None,
        }
    except Exception as e:
        return HTTPException(500, detail={
            "status": "Error",
            "data": f"{e}",
            "details": None,
        })
