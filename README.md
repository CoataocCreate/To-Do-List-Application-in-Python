### Project Title: To-Do List Application

#### Description
A simple command-line To-Do List Application built with Python using the `click` library for creating a CLI interface. Users can add tasks, mark tasks as done, delete tasks, and list all tasks.

#### Features
- **Add:** Add a new task to the to-do list.
- **List:** Display all tasks in the to-do list.
- **Done:** Mark a task as completed.
- **Delete:** Delete a task from the list.

#### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/todo_app.git
   cd todo_app
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows: venv\Scripts\activate
   # On macOS/Linux: source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # Install click library if not installed
   pip install click
   ```

#### Usage
- **Add a task:**
  ```bash
  python todo.py add "Buy groceries"
  ```
- **List tasks:**
  ```bash
  python todo.py list
  ```
- **Mark a task as done:**
  ```bash
  python todo.py done 1
  ```
- **Delete a task:**
  ```bash
  python todo.py delete 2
  ```

#### Examples
- **Adding a task:**
  ```bash
  $ python todo.py add "Buy groceries"
  Added task: Buy groceries
  ```
- **Listing tasks:**
  ```bash
  $ python todo.py list
  Tasks:
  1. Buy groceries
  ```
- **Marking a task as done:**
  ```bash
  $ python todo.py done 1
  Marked task "Buy groceries" as done.
  ```
- **Deleting a task:**
  ```bash
  $ python todo.py delete 1
  Deleted task "Buy groceries".
  ```

#### Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or a pull request on [GitHub](https://github.com/your_username/todo_app).

#### License
This project is licensed under the MIT License
