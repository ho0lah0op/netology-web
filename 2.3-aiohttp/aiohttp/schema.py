from abc import ABC
from typing import Optional

import pydantic


class AbstractAdvertisement(pydantic.BaseModel, ABC):
    title: str
    description: str
    owner: str

    @pydantic.field_validator('title')
    @classmethod
    def valid_title(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError(f'Title is too short, should be >3 characters')
        return v


class CreateAdvertisement(AbstractAdvertisement):
    title: str
    description: str
    owner: str


class UpdateAdvertisement(AbstractAdvertisement):
    title: Optional[str] = None
    description: Optional[str] = None
    owner: Optional[str] = None