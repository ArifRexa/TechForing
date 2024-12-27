from django.db import models
from django.utils.timezone import now

from accounts.models import CustomUser
from tasks.models import Task


# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.title}"
