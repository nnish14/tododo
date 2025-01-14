# tododo

A simple command-line interface (CLI) to-do list app written in Python. This app allows you to add, edit, finish, remove, and list tasks with support for due dates, priorities, and sorting.

## Features

- Add tasks with due dates and priorities.
- Edit existing tasks.
- Mark tasks as finished.
- Remove tasks.
- List tasks with filtering and sorting options.
- List finished tasks.
- Verbose and quiet output modes.
- Help command for usage information.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/tododo.git
   cd tododo
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

## Usage

1. **Add a Task**:
   ```sh
   ./todo.py add "Buy groceries due:2023-12-31 priority:high"
   ```

2. **List Tasks**:
   ```sh
   ./todo.py list --sort-by due
   ```

3. **Edit a Task**:
   ```sh
   ./todo.py edit 1 "Buy groceries and milk due:2023-12-31 priority:high"
   ```

4. **Finish a Task**:
   ```sh
   ./todo.py finish 1
   ```

5. **Remove a Task**:
   ```sh
   ./todo.py remove 1
   ```

6. **List Finished Tasks**:
   ```sh
   ./todo.py list --done
   ```

7. **Display Help**:
   ```sh
   ./todo.py -h
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
