# Project Management CLI

A Python-based Command-Line Interface (CLI) application for managing users, projects, and tasks. The application demonstrates Object-Oriented Programming (OOP), file persistence using JSON, command-line argument parsing, and modular software design.

## Features

* Create and manage users
* Create projects and assign them to users
* Create tasks and assign them to projects
* Mark tasks as completed
* Store data persistently using JSON
* Organize code using modules and classes
* Command-line interface using argparse

## Project Structure

```text
project_tracker/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── utils/
│   ├── __init__.py
│   └── storage.py
│
├── data/
│   └── database.json
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

## Classes

### User

Attributes:

* name
* email
* projects

Methods:

* add_project()
* remove_project()
* list_projects()

### Project

Attributes:

* title
* description
* due_date
* tasks

Methods:

* add_task()
* remove_task()
* list_tasks()

### Task

Attributes:

* title
* assigned_to
* status

Methods:

* mark_complete()

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd python_assesment
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

python main.py -h

## Usage Examples
### Create a User

```bash
python main.py add_user \
--name "Abdalla" \
--email "abdalla@gmail.com"
```

### List Users

```bash
python main.py list_users
```

### Add a Project

```bash
python main.py add_project \
--email "abdalla@gmail.com" \
--title "Expense Tracker" \
--description "Track personal expenses" \
--due-date "2026-07-01"
```

### List Projects

```bash
python main.py list_projects \
--email "abdalla@gmail.com"
```

### Add a Task

```bash
python main.py add_task \
--email "abdalla@gmail.com" \
--project "Expense Tracker" \
--title "Build Dashboard" \
--assigned-to "Abdalla"
```

### List Tasks

```bash
python main.py list_tasks \
--email "abdalla@gmail.com" \
--project "Expense Tracker"
```

### Complete a Task

```bash
python main.py complete_task \
--email "abdalla@gmail.com" \
--project "Expense Tracker" \
--task "Build Dashboard"
```

## Data Storage

The application stores data in:

```text
data/database.json
```

Data is automatically loaded and saved whenever users, projects, or tasks are created or updated.

## Technologies Used

* Python 3.10+
* argparse
* json
* Object-Oriented Programming (OOP)

## Problems Encountered
*Implementing the CLI interface (argparse), I had to revisit the topic to grasp the concept for implementation.

## Future Improvements

* Task priorities
* Due date validation
* Search functionality

## Author

Abdalla Msema
