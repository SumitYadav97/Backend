from fastapi import APIRouter, Depends

from app.core.deps import get_current_user
from app.schemas.course_schemas import Course

from app.services.course_service import (
    get_courses,
    create_course,
    update_course,
    delete_course
)
  
router = APIRouter(
    prefix="/course", 
    tags=["Course"]
)
 
 
@router.get("/")
def get_all_courses(
    current_user: dict = Depends(get_current_user)
):
    return get_courses()


@router.post("/")
def create(
    course: Course,
    current_user: dict = Depends(get_current_user)
):
    return create_course(course)


@router.put("/")
def update(
    course_id: int,
    course: Course,
    current_user: dict = Depends(get_current_user)
):
    return update_course(course_id, course)


@router.delete("/")
def delete(
    course_id: int,
    current_user: dict = Depends(get_current_user)
):
    return delete_course(course_id)