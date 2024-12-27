from django.contrib import admin
from tasks.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date')
    search_fields = ('title', 'status', 'priority', 'project__name', 'assigned_to__email')
