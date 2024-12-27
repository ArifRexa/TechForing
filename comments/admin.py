from django.contrib import admin

from comments.models import Comment


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'user', 'task', 'created_at')
    search_fields = ('user__email', 'task__title')
