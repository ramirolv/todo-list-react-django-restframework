from rest_framework import permissions

class UserViewSetPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Verificar si el usuario pertenece al grupo de administradores
        if request.user.is_superuser:
            # El usuario tiene permisos de administrador, permitir todas las acciones
            return True

        # Para otros usuarios, verificar los permisos específicos según la acción
        if request.method == 'GET':
            return request.user.has_perm('auth.view_user')
        elif request.method == 'POST':
            return request.user.has_perm('auth.add_user')
        elif request.method == 'PUT' or request.method == 'PATCH':
            return request.user.has_perm('auth.change_user')
        elif request.method == 'DELETE':
            return request.user.has_perm('auth.delete_user')

        return False