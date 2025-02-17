from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from projects.models import Project, ProjectMember
from projects.serializers import ProjectSerializer, ProjectMemberSerializer
from tasks.models import Task
from tasks.serializers import TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [IsAuthenticated]


class TaskListCreateView(generics.ListCreateAPIView):
    """
    GET: Retrieve all tasks for a specific project.
    POST: Create a new task in a specific project.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        return Task.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs["project_id"]
        serializer.save(project_id=project_id)
