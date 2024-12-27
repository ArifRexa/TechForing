from django.db import models
from django.utils.timezone import now

from accounts.models import CustomUser
from projects.models import Project


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ("To Do", "To Do"),
        ("In Progress", "In Progress"),
        ("Done", "Done"),
    ]
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="To Do")
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default="Medium")
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    created_at = models.DateTimeField(default=now)
    due_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} ({self.status})"