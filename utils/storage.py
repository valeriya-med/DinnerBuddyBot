import sqlite3
from config import DB_NAME

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        sql_request = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id integer NOT NULL,
        name text NOT NULL,
        date text NOT NULL,
        time text NOT NULL,
        guests_qty integer NOT NULL
        );"""
        conn.execute(sql_request)
        conn.commit()

user_data = {}

def init_user(user_id):
    user_data[user_id] = {}
    return user_data[user_id]

def get_user(user_id):
    return user_data.get(user_id, {})

def delete_user(user_id):
    user_data.pop(user_id, None)

def save_user(user_id):
    user = user_data.get(user_id)
    if not user:
        print(f"No data for user {user_id}")
        return
    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute(
                "INSERT INTO users (user_id, name, date, time, guests_qty) VALUES (?, ?, ?, ?, ?)",
                (user_id, user["name"], user["date"], user["time"], user["guests_qty"]),
        )
            conn.commit()
        print(f"User {user_id} saved to DB")
    except Exception as e:
        print(f"Error saving user {user_id}: {e}")
    finally:
        delete_user(user_id)
