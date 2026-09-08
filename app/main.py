from fastapi import FastAPI

from app.routers.students_routes import router as student_router
from app.routers.teaches_routes import router as teacher_router
from app.routers.course_route import router as course_router


app = FastAPI()

app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(course_router)


