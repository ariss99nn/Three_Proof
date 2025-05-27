from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permite solo a usuarios con rol 'ADMIN' modificar (POST, PUT, DELETE).
    Los demás usuarios autenticados solo pueden leer (GET).
    """
    def has_permission(self, request, view):
        # Si el método es seguro (GET, HEAD, OPTIONS), permitir siempre
        if request.method in permissions.SAFE_METHODS:
            return True
        # Para métodos no seguros (modificar), solo permitir si el usuario es admin
        return request.user.is_authenticated and request.user.role == 'ADMIN'
