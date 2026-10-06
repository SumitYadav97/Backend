from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class TeacherCreate(BaseModel):
    Name: str
    Subject: str
    Email: str
    Phone: str
    Salary: float
    JoiningDate: date

class TeacherUpdate(BaseModel):
    Name: Optional[str] = None
    Subject: Optional[str] = None
    Email: Optional[str] = None
    Phone: Optional[str] = None
    Salary: Optional[float] = None
    JoiningDate: Optional[date] = None

class TeacherResponse(BaseModel):
    TeacherID: int
    Name: str
    Subject: str
    Email: str
    Phone: str
    Salary: float
    JoiningDate: date