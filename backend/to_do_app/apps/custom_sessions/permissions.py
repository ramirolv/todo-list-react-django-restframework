from rest_framework import permissions

class UserViewSetPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Verificar si el usuario pertenece al grupo de administradores
        if request.user.is_superuser:
            # El usuario tiene permisos de administrador, permitir todas las acciones
            return True

        # Para otros usuarios, verificar los permisos específicos según la acción
        if request.method == 'GET':
            return request.user.has_perm('custom_sessions.view_customuser')
        elif request.method == 'POST':
            return request.user.has_perm('custom_sessions.add_customuser')
        elif request.method == 'PUT' or request.method == 'PATCH':
            return request.user.has_perm('custom_sessions.change_customuser')
        elif request.method == 'DELETE':
            return request.user.has_perm('custom_sessions.delete_customuser')

        return False