from fastapi import APIRouter, HTTPException, status
from app.schemas.students_schemas import Student
from app.services.students_services import (
    create_student,
    delete_student,
    get_students,
    update_student,
)

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/login")
def login_student(credentials: dict):
    username = credentials.get("username")
    password = credentials.get("password")
    
    # TODO: Validate student credentials against your database service
    return {"message": "Login successful", "access_token": "fake-jwt-token"}

@router.get("/")
def get_all_students():
    return get_students()

@router.post("/")
def add_student(student: Student):
    return create_student(student)

@router.put("/")
def update(student_id: int, student: Student):
    return update_student(student_id, student)

@router.delete("/")
def delete(student_id: int):
    return delete_student(student_id)