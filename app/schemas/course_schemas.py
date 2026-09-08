from pydantic import BaseModel


class Course(BaseModel):
    id: int
    name: str
    duration: str
    course_name: str