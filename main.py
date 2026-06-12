
from modules.User import User
from modules.Project import Project
from modules.Task import Task
from utils.storage import load_data, save_data

import argparse

# USER FUNCTIONS
def add_user(name, email):
    data = load_data()

    for user in data["users"]:
        if user["email"] == email:
            print("User already exists.")
            return

    user = User(name, email)
    data["users"].append(user.to_dict())
    save_data(data)
    print(f"User '{name}' added successfully.")


def list_users():
    data = load_data()
    users = data["users"]
    if not users:
        print("No users found.")
        return

    for user in users:
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print("-"*40)


# PROJECT FUNCTIONS
def add_project(user_email, title, description, due_date):
    data = load_data()

    for user in data["users"]:
        if user["email"] == user_email:
            project = Project(title, description, due_date)
            user["projects"].append(project.to_dict())

            save_data(data)
            print(f"Project '{title}' added successfully.")
            return

    print("User not found.")

def list_projects(email):
    data = load_data()
    for user in data["users"]:
        if not user["projects"]:
            print("No projects found for this user." )
            return
        
        print(f"\nProjects for {user['name']}")
        print("-"*40)
        for project in user["projects"]:
            print(f"Title: {project['title']}")
            print(f"Description: {project['description']}")
            print(f"Due Date: {project['due_date']}")
            print("-"*40)
        return
    print("User not found.")


# TASK FUNCTIONS
def add_task(email, project_title, title, assigned_to):
    data = load_data()

    for user in data["users"]:

        if user["email"] == email:
            for project in user["projects"]:
                if project["title"] == project_title:
                    task = Task(title, assigned_to)
                    project["tasks"].append(task.to_dict())
                    save_data(data)
                    print(f"Task '{title}' added successfully.")
                    return

    print("User or project not found.")


def list_tasks(email, project_title):
    data = load_data()

    for user in data["users"]:

        if user["email"] == email:
            for project in user["projects"]:
                if project["title"] == project_title:
                    if not project["tasks"]:
                        print("No tasks found for this project.")
                        return

                    print(f"\nTasks for {project['title']}")
                    print("-"*40)

                    for task in project["tasks"]:
                        print(f"Title: {task['title']}")
                        print(f"Status: {task['status']}")
                        print(f"Assigned To: {task['assigned_to']}")
                        print("-"*40)
                    return

    print("User or project not found.")


def complete_task(email, project_title, task_title):
    data = load_data()

    for user in data["users"]:

        if user["email"] == email:
            for project in user["projects"]:
                if project["title"] == project_title:
                    for task in project["tasks"]:
                        if task["title"] == task_title:
                            task["status"] = "Completed"
                            save_data(data)
                            print(f"Task '{task_title}' completed successfully.")
                            return

    print("User or project or task not found.")


# CLI setup

def main():

    parser = argparse.ArgumentParser(
        description="Task Management System"
    )

    subparsers = parser.add_subparsers(dest="command")

    # USER COMMANDS
    add_user_parser = subparsers.add_parser("add_user")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)

    subparsers.add_parser("list_users")

    # PROJECT COMMANDS
    add_project_parser = subparsers.add_parser("add_project")
    add_project_parser.add_argument("--email", required=True)
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.add_argument("--due_date", required=True)

    list_projects_parser = subparsers.add_parser("list_projects")
    list_projects_parser.add_argument("--email", required=True)

    # TASK COMMANDS
    add_task_parser = subparsers.add_parser("add_task")
    add_task_parser.add_argument("--email", required=True)
    add_task_parser.add_argument("--project_title", required=True)
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument("--assigned_to", required=True)

    list_tasks_parser = subparsers.add_parser("list_tasks")
    list_tasks_parser.add_argument("--email", required=True)
    list_tasks_parser.add_argument("--project_title", required=True)

    complete_task_parser = (
        subparsers.add_parser("complete_task")
    )
    complete_task_parser.add_argument("--email", required=True)
    complete_task_parser.add_argument("--project_title", required=True)
    complete_task_parser.add_argument("--task", required=True)

    args = parser.parse_args()

    # Command router
    if args.command == "add_user":
        add_user(args.name, args.email)
    elif args.command == "list_users":
        list_users()
    elif args.command == "add_project":
        add_project(args.email, args.title, args.description, args.due_date)
    elif args.command == "list_projects":
        list_projects(args.email)
    elif args.command == "add_task":
        add_task(args.email, args.project_title, args.title, args.assigned_to)
    elif args.command == "list_tasks":
        list_tasks(args.email, args.project_title)
    elif args.command == "complete_task":
        complete_task(args.email, args.project_title, args.task)

    else :
        parser.print_help()

if __name__ == "__main__":
    main()