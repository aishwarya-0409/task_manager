from flask import Flask, render_template_string, request, redirect, url_for # type: ignore
from db import init_db, add_task, list_tasks, delete_task
from datetime import datetime

init_db()
app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Task Manager Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #f9f9fc;
            --card: #ffffff;
            --text: #2e2e2e;
            --accent: #6c63ff;
            --border: #e0e0e0;
            --completed: #a0a0a0;
        }
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            padding: 2rem;
            color: var(--text);
        }
        h1 {
            margin-bottom: 1rem;
            color: var(--accent);
        }
        form {
            margin-bottom: 1rem;
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        input, select, button {
            padding: 0.5rem 0.75rem;
            border: 1px solid var(--border);
            border-radius: 5px;
            font-size: 1rem;
        }
        button {
            background-color: var(--accent);
            color: white;
            border: none;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        button:hover {
            background-color: #5753d8;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background-color: var(--card);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
        th, td {
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }
        th {
            background-color: #f1f1f8;
        }
        .completed {
            text-decoration: line-through;
            color: var(--completed);
        }
        @media (max-width: 600px) {
            table, thead, tbody, th, td, tr {
                display: block;
            }
            th {
                display: none;
            }
            td {
                border: none;
                padding: 0.5rem;
                position: relative;
            }
            td::before {
                content: attr(data-label);
                font-weight: bold;
                display: block;
                margin-bottom: 0.25rem;
            }
        }
    </style>
</head>
<body>
    <h1>📝 Task Manager</h1>

    <form method="POST" action="/add">
        <input name="title" placeholder="Task title" required>
        <input name="due_date" type="date">
        <button type="submit">Add</button>
    </form>

    <form method="GET" action="/">
        <select name="filter">
            <option value="all">All</option>
            <option value="pending">Pending</option>
            <option value="completed">Completed</option>
        </select>
        <select name="sort">
            <option value="id">Sort by ID</option>
            <option value="due">Sort by Due Date</option>
        </select>
        <button type="submit">Apply</button>
    </form>

    <table>
        <thead>
            <tr>
                <th>ID</th><th>Title</th><th>Due Date</th><th>Status</th><th>Action</th>
            </tr>
        </thead>
        <tbody>
        {% for t in tasks %}
        <tr>
            <td data-label="ID">{{ t['id'] }}</td>
            <td data-label="Title" class="{% if t['completed'] %}completed{% endif %}">{{ t['title'] }}</td>
            <td data-label="Due Date">{{ t['due_date'] or '-' }}</td>
            <td data-label="Status">{{ '✅ Completed' if t['completed'] else '🕒 Pending' }}</td>
            <td data-label="Action">
                <form method="POST" action="/delete/{{ t['id'] }}" style="display:inline;">
                    <button type="submit">🗑️</button>
                </form>
            </td>
        </tr>
        {% endfor %}
        </tbody>
    </table>
</body>
</html>
'''


@app.route('/', methods=['GET'])
def index():
    filter_val = request.args.get('filter', 'all')
    sort_val = request.args.get('sort', 'id')
    show_completed = None
    if filter_val == 'pending':
        show_completed = False
    elif filter_val == 'completed':
        show_completed = True
    sort_by_due = sort_val == 'due'
    tasks = list_tasks(show_completed, sort_by_due)
    return render_template_string(TEMPLATE, tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    due_date = request.form.get('due_date') or None
    add_task(title, due_date)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
