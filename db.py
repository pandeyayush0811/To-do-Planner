import sqlite3

def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

def create_table():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_task(task):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", (task, False))
    conn.commit()
    conn.close()

def get_tasks():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return tasks

def update_task_status(task_id, status):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
