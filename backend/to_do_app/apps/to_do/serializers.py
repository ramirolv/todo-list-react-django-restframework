from rest_framework import serializers
from .models import Project, Board, Column, Task, Attachment, Checklist, ToDoItem
from apps.custom_sessions.serializers import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'owner']
        read_only_fields = ['created_at', 'updated_at', 'owner']

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = '__all__'

class ChecklistSerializer(serializers.ModelSerializer):
    items = ToDoItemSerializer(many=True, read_only=True)

    class Meta:
        model = Checklist
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)
    checklists = ChecklistSerializer(many=True, read_only=True)
    assigned_to = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'