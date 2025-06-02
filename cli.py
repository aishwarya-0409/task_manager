import argparse
from db import init_db, add_task, list_tasks, complete_task
from datetime import datetime

init_db()

def main():
    parser = argparse.ArgumentParser(description='Task Manager CLI')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', type=str, help='Task title')
    add_parser.add_argument('--due', type=str, help='Due date (YYYY-MM-DD)', default=None)

    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('--completed', action='store_true', help='Show only completed tasks')
    list_parser.add_argument('--pending', action='store_true', help='Show only pending tasks')
    list_parser.add_argument('--sort', action='store_true', help='Sort by due date')

    complete_parser = subparsers.add_parser('complete', help='Mark a task as completed')
    complete_parser.add_argument('id', type=int, help='Task ID')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.title, args.due)
        print('Task added.')
    elif args.command == 'list':
        show_completed = None
        if args.completed:
            show_completed = True
        elif args.pending:
            show_completed = False
        tasks = list_tasks(show_completed, sort_by_due=args.sort)
        for t in tasks:
            status = '✓' if t['completed'] else ' '
            due = t['due_date'] if t['due_date'] else '-'
            print(f"[{status}] {t['id']}: {t['title']} (Due: {due})")
    elif args.command == 'complete':
        complete_task(args.id)
        print('Task marked as completed.')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
