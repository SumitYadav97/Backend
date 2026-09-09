from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.students_routes import router as student_router
from app.routers.teaches_routes import router as teacher_router
from app.routers.course_route import router as course_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(course_router)