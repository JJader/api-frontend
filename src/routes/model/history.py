# teste.py

import psycopg2
from psycopg2.extras import RealDictCursor
import pickle
from fastapi import APIRouter


def memoryview_to_bytes(mv):
    try:
        data = pickle.loads(mv.tobytes())
    except Exception:
        data = mv.tobytes().decode("unicode_escape").encode("latin1").decode("utf-8")

    return str(data)


def datetime_to_str(dt):
    return dt.isoformat()


def convert_to_json(data):

    converted_data = []
    for item in data:
        try:
            new_item = {
                "task_id": item["task_id"],
                "date_done": datetime_to_str(item["date_done"]),
                "result": memoryview_to_bytes(item["result"]),
                "status": item["status"],
                "args": memoryview_to_bytes(item["args"]),
                "kwargs": memoryview_to_bytes(item["kwargs"]),
            }
        except Exception:
            new_item = {}

        converted_data.append(new_item)

    return converted_data


router = APIRouter()


@router.get("/model/history")
async def read_history():

    conn = psycopg2.connect(
        dbname="mydatabase",
        user="myuser",
        password="mypassword",
        host="db",
        port="5432",
    )

    cursor = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cursor.execute(
            """
            SELECT *
            FROM celery_taskmeta
            WHERE name = 'app.mlflow.tasks.predict'
        """
        )
        json_result = convert_to_json(cursor.fetchall())
        return json_result

    finally:
        cursor.close()
        conn.close()
