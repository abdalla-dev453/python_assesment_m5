
class Task:
    def __init__(self, title,assigned_to):
        self.title = title
        self.status = "Pending"
        self.assigned_to = assigned_to

    def mark_complete(self):
        self.status = "Completed"

    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Status: {self.status}\n"
            f"Assigned to: {self.assigned_to}\n"
        )