
from os.path import abspath
from pathlib import Path

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ABSPATH_DATABASE = "///" + str(Path(abspath(__file__)).parent) + "/"

Base = declarative_base()
engine = create_engine(F"sqlite:{ABSPATH_DATABASE}system_glaucio.db", echo=False)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)

class CreateSession:
    def create_session():
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()