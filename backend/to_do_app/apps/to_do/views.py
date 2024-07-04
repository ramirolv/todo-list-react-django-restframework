from django.utils import timezone
from rest_framework import viewsets, permissions
from rest_framework.permissions import DjangoModelPermissions
from .models import Project, Board, Column, Task, Attachment, Checklist, ToDoItem
from .serializers import ProjectSerializer, BoardSerializer, ColumnSerializer, TaskSerializer, AttachmentSerializer, ChecklistSerializer, ToDoItemSerializer

class CustomDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map = {
            'GET': ['%(app_label)s.view_%(model_name)s'],
            'OPTIONS': [],
            'HEAD': [],
            'POST': ['%(app_label)s.add_%(model_name)s'],
            'PUT': ['%(app_label)s.change_%(model_name)s'],
            'PATCH': ['%(app_label)s.change_%(model_name)s'],
            'DELETE': ['%(app_label)s.delete_%(model_name)s'],
        }

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [CustomDjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [CustomDjangoModelPermissions]

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = [CustomDjangoModelPermissions]

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [CustomDjangoModelPermissions]

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [CustomDjangoModelPermissions]

class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    permission_classes = [CustomDjangoModelPermissions]

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())

class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [CustomDjangoModelPermissions]

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())