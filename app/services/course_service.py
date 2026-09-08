from fastapi import HTTPException

from app.utils.utils import read_json, write_json


FILE = "app/data/courses.json"


# GET ALL COURSES
def get_courses():

    return read_json(FILE)


# CREATE COURSE
def create_course(course):

    courses = read_json(FILE)

    courses.append(course.model_dump())

    write_json(FILE, courses)

    return {
        "message": "Course added successfully",
        "course": course.model_dump()
    }


# UPDATE COURSE
def update_course(course_id: int, course):

    courses = read_json(FILE)

    for course_data in courses:

        if course_data["id"] == course_id:

            course_data["name"] = course.name
            course_data["duration"] = course.duration
            course_data["course_name"] = course.course_name

            write_json(FILE, courses)

            return {
                "message": "Course updated successfully",
                "course": course_data
            }

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


# DELETE COURSE
def delete_course(course_id: int):

    courses = read_json(FILE)

    for course_data in courses:

        if course_data["id"] == course_id:

            courses.remove(course_data)

            write_json(FILE, courses)

            return {
                "message": "Course deleted successfully",
                "course": course_data
            }

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )