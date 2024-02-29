import os
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm.session import sessionmaker
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, Text, VARCHAR
from sqlalchemy.orm import declarative_base


load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

PG_DSN = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_async_engine(PG_DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = sqlalchemy.orm.declarative_base()


class SwapiCharacters(Base):
    __tablename__ = 'swapi_characters'
    id = Column(Integer, primary_key=True)
    birth_year = Column(VARCHAR(10))
    eye_color = Column(String)
    films = Column(Text)
    gender = Column(VARCHAR(25))
    hair_color = Column(String)
    height = Column(VARCHAR(10))
    homeworld = Column(VARCHAR(50))
    mass = Column(VARCHAR(10))
    name = Column(VARCHAR(50))
    skin_color = Column(String)
    species = Column(Text)
    starships = Column(Text)
    vehicles = Column(Text)
