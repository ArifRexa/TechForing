from django.urls import path
from projects.views import ProjectViewSet, ProjectMemberViewSet, TaskListCreateView

urlpatterns = [
    path('', ProjectViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('<int:pk>/members/', ProjectMemberViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:project_pk>/members/<int:pk>/', ProjectMemberViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('<int:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
]
