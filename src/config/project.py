import os

from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

PROJECT = os.getenv("PROJECT")
VERSION = os.getenv("VERSION")
DESCRIPTION = os.getenv("DESCRIPTION")
DEBUG = True if int(os.getenv("DEBUG")) else False
PORT = int(os.getenv("PORT"))
ALLOW_ORIGINS = os.getenv("ALLOW_ORIGINS")
LINK_FORM_TESTIMONI = os.getenv("LINK_FORM_TESTIMONI")
SECRET_PARAM = os.getenv("SECRET_PARAM")
SECRET_VAL = os.getenv("SECRET_VAL")
