import sys
import json
import os
import argparse
from datetime import datetime

# Task Class
class Task:
    def __init__(self, task_id, text, due_date=None, priority=None, done=False):
        self.task_id = task_id
        self.text = text
        self.due_date = due_date
        self.priority = priority
        self.done = done

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'text': self.text,
            'due_date': self.due_date,
            'priority': self.priority,
            'done': self.done
        }

    @staticmethod
    def from_dict(data):
        return Task(data['task_id'], data['text'], data['due_date'], data['priority'], data['done'])

# File Management
TASK_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        tasks_data = json.load(file)
        return [Task.from_dict(data) for data in tasks_data]

def save_tasks(tasks):
    tasks_data = [task.to_dict() for task in tasks]
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks_data, file, indent=4)

# Task Management Functions
def add_task(tasks, text, due_date=None, priority=None):
    task_id = len(tasks) + 1
    task = Task(task_id, text, due_date, priority)
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added: {task.text}')

def edit_task(tasks, task_id, new_text):
    task = next((t for t in tasks if t.task_id == int(task_id)), None)
    if task:
        task.text = new_text
        save_tasks(tasks)
        print(f'Task edited: {task.text}')
    else:
        print(f'Error: Task with ID {task_id} not found')

def finish_task(tasks, task_id):
    task = next((t for t in tasks if t.task_id == int(task_id)), None)
    if task:
        task.done = True
        save_tasks(tasks)
        print(f'Task finished: {task.text}')
    else:
        print(f'Error: Task with ID {task_id} not found')

def remove_task(tasks, task_id):
    global TASK_FILE
    task = next((t for t in tasks if t.task_id == int(task_id)), None)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        if not tasks:
            os.remove(TASK_FILE)
        print(f'Task removed: {task.text}')
    else:
        print(f'Error: Task with ID {task_id} not found')

def list_tasks(tasks, grep=None, sort_by=None, verbose=False, quiet=False, done=False):
    filtered_tasks = [t for t in tasks if t.done == done]
    if grep:
        filtered_tasks = [t for t in filtered_tasks if grep in t.text]
    if sort_by:
        filtered_tasks = sorted(filtered_tasks, key=lambda t: getattr(t, sort_by) or '')
    for task in filtered_tasks:
        print(f'{task.task_id}: {task.text}')
        if verbose:
            print(f'  Due Date: {task.due_date}')
            print(f'  Priority: {task.priority}')
            print(f'  Status: {"Done" if task.done else "Pending"}')

# Command-Line Interface
def parse_arguments():
    parser = argparse.ArgumentParser(description='CLI To-Do List App')
    subparsers = parser.add_subparsers(dest='command')

    # Add Task
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('text', help='Task text')
    parser_add.add_argument('--due', help='Due date (YYYY-MM-DD)')
    parser_add.add_argument('--priority', help='Priority level')

    # Edit Task
    parser_edit = subparsers.add_parser('edit', help='Edit an existing task')
    parser_edit.add_argument('task_id', help='Task ID')
    parser_edit.add_argument('new_text', help='New task text')

    # Finish Task
    parser_finish = subparsers.add_parser('finish', help='Mark a task as finished')
    parser_finish.add_argument('task_id', help='Task ID')

    # Remove Task
    parser_remove = subparsers.add_parser('remove', help='Remove a task')
    parser_remove.add_argument('task_id', help='Task ID')

    # List Tasks
    parser_list = subparsers.add_parser('list', help='List tasks')
    parser_list.add_argument('--grep', help='Filter tasks containing the specified word')
    parser_list.add_argument('--sort-by', choices=['due', 'priority'], help='Sort tasks by due date or priority')
    parser_list.add_argument('--verbose', action='store_true', help='Print more detailed output')
    parser_list.add_argument('--quiet', action='store_true', help='Print less detailed output')
    parser_list.add_argument('--done', action='store_true', help='List finished tasks instead of unfinished ones')

    return parser.parse_args()

# Main Function
def main():
    parser = argparse.ArgumentParser(description='CLI To-Do List App')
    parser.add_argument('-h', '--help', action='help', help='Show this help message and exit')
    subparsers = parser.add_subparsers(dest='command')

    # Add Task
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('text', help='Task text')
    parser_add.add_argument('--due', help='Due date (YYYY-MM-DD)')
    parser_add.add_argument('--priority', help='Priority level')

    # Edit Task
    parser_edit = subparsers.add_parser('edit', help='Edit an existing task')
    parser_edit.add_argument('task_id', help='Task ID')
    parser_edit.add_argument('new_text', help='New task text')

    # Finish Task
    parser_finish = subparsers.add_parser('finish', help='Mark a task as finished')
    parser_finish.add_argument('task_id', help='Task ID')

    # Remove Task
    parser_remove = subparsers.add_parser('remove', help='Remove a task')
    parser_remove.add_argument('task_id', help='Task ID')

    # List Tasks
    parser_list = subparsers.add_parser('list', help='List tasks')
    parser_list.add_argument('--grep', help='Filter tasks containing the specified word')
    parser_list.add_argument('--sort-by', choices=['due', 'priority'], help='Sort tasks by due date or priority')
    parser_list.add_argument('--verbose', action='store_true', help='Print more detailed output')
    parser_list.add_argument('--quiet', action='store_true', help='Print less detailed output')
    parser_list.add_argument('--done', action='store_true', help='List finished tasks instead of unfinished ones')

    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == 'add':
        add_task(tasks, args.text, args.due, args.priority)
    elif args.command == 'edit':
        edit_task(tasks, args.task_id, args.new_text)
    elif args.command == 'finish':
        finish_task(tasks, args.task_id)
    elif args.command == 'remove':
        remove_task(tasks, args.task_id)
    elif args.command == 'list':
        list_tasks(tasks, args.grep, args.sort_by, args.verbose, args.quiet, args.done)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
