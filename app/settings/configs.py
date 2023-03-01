
import os

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates


class Configs(BaseSettings):


    ModeloBase: declarative_base = declarative_base()

    user: str = os.getenv("MYSQL_USER")
    passwd: str = os.getenv("MYSQL_PASS")
    host: str = os.getenv("MYSQL_HOST")
    port: str = os.getenv("MYSQL_PORT")
    database: str = os.getenv("MYSQL_DB")

    DB_URL: str = f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}"
    
    TEMPLATES: Jinja2Templates = Jinja2Templates(directory="templates")

    SALT: str = "systemglaucio"

    class Config:
        case_sensitive: bool = True


config: Configs = Configs()