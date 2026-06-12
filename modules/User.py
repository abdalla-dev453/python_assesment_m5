
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def remove_project(self, project_title):
        self.projects = [
            project for project in self.projects if project.title != project_title
        ]


    def list_projects(self):
        if not self.projects:
            print("No projects found for this user.")
    
        for project in self.projects:
            print(project)
        return


    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "projects": [project.to_dict() for project in self.projects]
        }


    def __str__(self):
        return f"{self.name} | ({self.email})"