# Task Manager CLI & Web Dashboard

## Overview
This project is a Python-based Task Manager that provides both a command-line interface (CLI) and a web dashboard (Flask). Both interfaces share a single SQLite database (`tasks.db`) for persistent storage, ensuring all changes are reflected across both interfaces.

## Approach
- **Database:** Used SQLite for lightweight, file-based persistent storage. All task operations (add, list, complete, delete) are performed via SQL queries in `db.py`.
- **CLI:** The CLI (`cli.py`) allows users to add, list, and complete tasks. It uses Python's `argparse` for command parsing and interacts with the database through functions in `db.py`.
- **Web Dashboard:** The web dashboard (`web_dashboard.py`) is built with Flask and provides a modern, responsive UI for managing tasks. Users can add, view, delete, and filter tasks, as well as sort by due date or status. The dashboard uses HTML/CSS for styling and Flask's templating for dynamic content.
- **Integration:** Both the CLI and web dashboard import and use the same database logic from `db.py`, ensuring data consistency.

## How to Run
1. **Install dependencies:**
   ```powershell
   pip install flask
   ```
2. **Run the CLI:**
   ```powershell
   python cli.py add "Sample Task" --due 2025-06-01
   python cli.py list
   python cli.py complete <id>
   ```
3. **Run the Web Dashboard:**
   ```powershell
   python web_dashboard.py
   ```
   Then open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## Libraries/Frameworks Used
- [Flask](https://flask.palletsprojects.com/) (web framework)
- [SQLite3](https://docs.python.org/3/library/sqlite3.html) (built-in Python library for database)
- [argparse](https://docs.python.org/3/library/argparse.html) (built-in Python library for CLI parsing)

## Live Links / APK
- This is a local project. No live link or APK is provided. To use, run locally as described above.

## Features
- Add, list, and complete tasks via CLI
- View, add, delete, filter, and sort tasks via web dashboard
- Due date support
- Shared persistent storage

---

