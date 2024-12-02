from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional

class UserBase(BaseModel):
    email: EmailStr
    username: str
    interest_tags: List[str] = []

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ProgramBase(BaseModel):
    title: str
    platform: str
    date_time: datetime
    registration_method: str
    categories: List[str]
    description: Optional[str] = None

class ProgramCreate(ProgramBase):
    pass

class ProgramResponse(ProgramBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
