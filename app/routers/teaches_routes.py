from fastapi import APIRouter, Depends, status
from typing import List
import pyodbc

from app.connection.connection import get_db
from app.schemas.teachers_schemas import TeacherCreate, TeacherUpdate, TeacherResponse
from app.services.teachers_services import (
    get_all_teachers,
    get_teacher_by_id,
    create_teacher,
    update_teacher,
    delete_teacher
)


router = APIRouter(prefix="/teachers", tags=["Teachers"])


@router.get("/", response_model=List[TeacherResponse])
def read_all(conn: pyodbc.Connection = Depends(get_db)):
    return get_all_teachers(conn)


@router.get("/", response_model=TeacherResponse)
def read_one(teacher_id: int, conn: pyodbc.Connection = Depends(get_db)):
    return get_teacher_by_id(teacher_id, conn)


@router.post("/", response_model=TeacherResponse, status_code=status.HTTP_201_CREATED)
def create(data: TeacherCreate, conn: pyodbc.Connection = Depends(get_db)):
    return create_teacher(data, conn)


@router.put("/", response_model=TeacherResponse)
def update(teacher_id: int, data: TeacherUpdate, conn: pyodbc.Connection = Depends(get_db)):
    return update_teacher(teacher_id, data, conn)
 

@router.delete("/")
def delete(teacher_id: int, conn: pyodbc.Connection = Depends(get_db)):
    return delete_teacher(teacher_id, conn)