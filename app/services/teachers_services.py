import pyodbc
from fastapi import HTTPException
from app.schemas.teachers_schemas import TeacherCreate, TeacherUpdate

def get_all_teachers(conn: pyodbc.Connection):
    with conn.cursor() as cursor:
        cursor.execute("SELECT TeacherID, Name, Subject, Email, Phone, Salary, JoiningDate FROM Teachers")
        rows = cursor.fetchall()
        return [
            {
                "TeacherID": r[0],
                "Name": r[1],
                "Subject": r[2],
                "Email": r[3],
                "Phone": r[4],
                "Salary": float(r[5]),
                "JoiningDate": r[6]
            }
            for r in rows
        ]

def get_teacher_by_id(teacher_id: int, conn: pyodbc.Connection):
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT TeacherID, Name, Subject, Email, Phone, Salary, JoiningDate FROM Teachers WHERE TeacherID = ?",
            (teacher_id,)
        )
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Teacher not found")
        return {
            "TeacherID": row[0],
            "Name": row[1],
            "Subject": row[2],
            "Email": row[3],
            "Phone": row[4],
            "Salary": float(row[5]),
            "JoiningDate": row[6]
        }

def create_teacher(data: TeacherCreate, conn: pyodbc.Connection):
    with conn.cursor() as cursor:
        query = """
            INSERT INTO Teachers (Name, Subject, Email, Phone, Salary, JoiningDate)
            OUTPUT INSERTED.TeacherID, INSERTED.Name, INSERTED.Subject, INSERTED.Email, INSERTED.Phone, INSERTED.Salary, INSERTED.JoiningDate
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (data.Name, data.Subject, data.Email, data.Phone, data.Salary, data.JoiningDate))
        row = cursor.fetchone()
        conn.commit()
        return {
            "TeacherID": row[0],
            "Name": row[1],
            "Subject": row[2],
            "Email": row[3],
            "Phone": row[4],
            "Salary": float(row[5]),
            "JoiningDate": row[6]
        }

def update_teacher(teacher_id: int, data: TeacherUpdate, conn: pyodbc.Connection):
    existing = get_teacher_by_id(teacher_id, conn)
    
    name = data.Name if data.Name is not None else existing["Name"]
    subject = data.Subject if data.Subject is not None else existing["Subject"]
    email = data.Email if data.Email is not None else existing["Email"]
    phone = data.Phone if data.Phone is not None else existing["Phone"]
    salary = data.Salary if data.Salary is not None else existing["Salary"]
    joining_date = data.JoiningDate if data.JoiningDate is not None else existing["JoiningDate"]

    with conn.cursor() as cursor:
        query = """
            UPDATE Teachers
            SET Name = ?, Subject = ?, Email = ?, Phone = ?, Salary = ?, JoiningDate = ?
            WHERE TeacherID = ?
        """
        cursor.execute(query, (name, subject, email, phone, salary, joining_date, teacher_id))
        conn.commit()
        return {
            "TeacherID": teacher_id,
            "Name": name,
            "Subject": subject,
            "Email": email,
            "Phone": phone,
            "Salary": float(salary),
            "JoiningDate": joining_date
        }

def delete_teacher(teacher_id: int, conn: pyodbc.Connection):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM Teachers WHERE TeacherID = ?", (teacher_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Teacher not found")
        conn.commit()
        return {"message": "Teacher deleted successfully", "TeacherID": teacher_id}