from fastapi import APIRouter, Depends

from auth.base_config import current_user
from tasks.task import send_email_report

router = APIRouter(prefix="/test")


@router.get("/send_email")
async def send_email(user=Depends(current_user)):
    send_email_report.delay(user.name)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }