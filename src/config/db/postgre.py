import urllib.parse
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(dotenv_path="./.env")

DB_USERNAME = os.getenv("POSTGRESQL_DB_USERNAME")
DB_PASSWORD = os.getenv("POSTGRESQL_DB_PASSWORD")
DB_HOST = os.getenv("POSTGRESQL_DB_HOST")
DB_PORT = os.getenv("POSTGRESQL_DB_PORT")
DB = os.getenv("POSTGRESQL_DB")
DB_SCHEMA = os.getenv("POSTGRESQL_DB_SCHEMA")

URI = None
if DB_HOST not in ["127.0.0.1", "localhost"]:
    URI = f"postgresql+psycopg2://{DB_USERNAME}:{urllib.parse.quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB}?sslmode=require"
else:
    URI = f"postgresql+psycopg2://{DB_USERNAME}:{urllib.parse.quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB}"

engine = create_engine(url=URI, pool_pre_ping=True)
session = sessionmaker(bind=engine)
session = session()
