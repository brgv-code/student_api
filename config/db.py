# create a mysql database connection from sqlalchemy to an endpoint in the database

from sqlalchemy import create_engine,MetaData
from pydantic import BaseSettings


engine = create_engine("mysql+pymysql://root:$$@localhost:3306/py_crud")
meta = MetaData()
con = engine.connect()

#create a config class for .env file

class Settings(BaseSettings):
    app_name: str = "FastAPI CRUD"
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"