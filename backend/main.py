from fastapi import FastAPI
import sqlite3
import os

app = FastAPI()

DB_PATH = os.path.join("..", "database", "test.db")

@app.get("/")
def home():
    return {"message": "API works"}

@app.get("/athlete/{am}")
def get_athlete(am: int):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT firstName, Surname, AM FROM test WHERE AM=?",
        (am,)
    )

    row = cursor.fetchone()
    conn.close()

    if not row:
        return {"found": False}

    return {
        "found": True,
        "firstName": row[0],
        "surname": row[1],
        "AM": row[2]
    }
