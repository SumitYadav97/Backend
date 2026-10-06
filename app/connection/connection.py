import pyodbc

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=teachers;"
    "Trusted_Connection=yes;"
)

def get_db():
    conn = pyodbc.connect(CONNECTION_STRING)
    try:
        yield conn
    finally:
        conn.close()