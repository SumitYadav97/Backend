from app.utils.utils import read_json, write_json


FILE = "app/data/students.json"


def get_students():

    return read_json(FILE)


def create_student(student):

    students = read_json(FILE)

    students.append(student.model_dump())

    write_json(FILE, students)

    return {
        "message": "Student added successfully",
        "student": student.model_dump()
    }


def update_student(student_id: int, student):

    students = read_json(FILE)

    for student_data in students:

        if student_data["id"] == student_id:

            student_data["name"] = student.name
            student_data["age"] = student.age
            student_data["city"] = student.city

            write_json(FILE, students)

            return {
                "message": "Student updated successfully",
                "student": student_data
            }



def delete_student(student_id: int):

    students = read_json(FILE)

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            write_json(FILE, students)

            return {
                "message": "Student deleted successfully",
                "student": student
            }

