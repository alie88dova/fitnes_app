from dotenv import load_dotenv
import os


load_dotenv()

USER = os.environ.get("USER")
PASS = os.environ.get("PASS")
ADDRESS = os.environ.get("ADDRESS")
BASE_NAME = os.environ.get("BASE_NAME")
SECRET = os.environ.get("SECRET")