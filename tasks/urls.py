from django.urls import path

from comments.views import CommentViewSet
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('<int:id>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/comments/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'post': 'create'})),
]
