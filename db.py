import sqlite3
from datetime import datetime

DB_NAME = 'tasks.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due_date TEXT,
            completed INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title, due_date=None):
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (title, due_date) VALUES (?, ?)', (title, due_date))
    conn.commit()
    conn.close()

def list_tasks(show_completed=None, sort_by_due=False):
    conn = get_db_connection()
    query = 'SELECT * FROM tasks'
    params = []
    if show_completed is not None:
        query += ' WHERE completed = ?'
        params.append(1 if show_completed else 0)
    if sort_by_due:
        query += ' ORDER BY due_date ASC'
    else:
        query += ' ORDER BY id ASC'
    tasks = conn.execute(query, params).fetchall()
    conn.close()
    return tasks

def complete_task(task_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
