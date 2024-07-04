from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsProjectMember(permissions.BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_pk')
        if project_id:
            return request.user.projects.filter(id=project_id).exists()
        return True

    def has_object_permission(self, request, view, obj):
        return request.user.projects.filter(id=obj.project.id).exists()