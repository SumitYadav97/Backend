from fastapi import APIRouter

from app.schemas.teachers_schemas import Teacher
from app.services.teachers_services import (
    create_teacher,
    delete_teacher,
    get_teachers,
    update_teacher,
)

router = APIRouter(prefix="/teachers",tags=["teachers"])

@router.get("/")
def get_all_teachers():
    return get_teachers()


@router.post("/")
def add_teacher(teacher: Teacher):
    return create_teacher(teacher)

@router.put("/")
def update_teacher_route(teacher_id: int, teacher: Teacher):
    return update_teacher(teacher_id, teacher)

@router.delete("/")
def delete_teacher_route(teacher_id: int):
    return delete_teacher(teacher_id)