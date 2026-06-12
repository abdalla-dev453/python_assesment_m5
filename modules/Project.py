

class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_title):
        self.tasks = [
            task for task in self.tasks if task.title != task_title
        ]


    def list_tasks(self):
        if not self.tasks:
            print("No tasks found for this project.")

        for task in self.tasks:
            print(task)
        return


    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    
    def __str__(self):
        return (
            f"Project: {self.title}\n"
            f"Due Date: {self.due_date}\n"
        )