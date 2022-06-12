from ast import Str
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    user = "user"
    student = "student"
    admin = "admin"

class UserUpdateRequest(BaseModel):
    first_name = Optional[str]
    last_name = Optional[str]
    middle_name = Optional[str]
    roles = Optional[List[str]]

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]