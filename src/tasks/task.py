import smtplib
from email.message import EmailMessage

from celery import Celery
from config import SMTP_USER, SMTP_PASSWORD

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = "Регистрация в приложение fitnes app"
    email['From'] = SMTP_USER
    email['To'] = "a_lie@bk.ru"
    #TODO Сделать такую же штуку для регестрации
    email.set_content(
        "<div>"
        f"<h2>Привет {username}</h2>"
        f"</div>"
    )
    return email


@celery.task
def send_email_report(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as sm_server:
        sm_server.login(SMTP_USER, SMTP_PASSWORD)
        sm_server.send_message(email)

