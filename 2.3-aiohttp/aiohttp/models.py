import datetime
import os

import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

load_dotenv()

POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '123456')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'app')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', '127.0.0.1')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

PG_DSN = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_async_engine(PG_DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = sqlalchemy.orm.declarative_base()


class Advertisement(Base):
    __tablename__ = 'advertisement'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    owner: Mapped[str] = mapped_column(String(50), nullable=False)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())

    @property
    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'owner': self.owner,
            'creation_date': self.creation_date.isoformat(),
        }


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
