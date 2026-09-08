from app.utils.utils import read_json, write_json


FILE = "app/data/teachers.json"


def get_teachers():

    return read_json(FILE)


def create_teacher(teacher):

    teachers = read_json(FILE)

    teachers.append(teacher.model_dump())

    write_json(FILE, teachers)

    return {
        "message": "Teacher added successfully",
        "teacher": teacher.model_dump()
    }


def update_teacher(teacher_id: int, teacher):

    teachers = read_json(FILE)

    for teacher_data in teachers:

        if teacher_data["id"] == teacher_id:

            teacher_data["name"] = teacher.name
            teacher_data["subject"] = teacher.subject
            teacher_data["experience"] = teacher.experience

            write_json(FILE, teachers)

            return {
                "message": "Teacher updated successfully",
                "teacher": teacher_data
            }

    return None


def delete_teacher(teacher_id: int):

    teachers = read_json(FILE)

    for teacher in teachers:

        if teacher["id"] == teacher_id:

            teachers.remove(teacher)

            write_json(FILE, teachers)

            return {
                "message": "Teacher deleted successfully",
                "teacher": teacher
            }

    return None