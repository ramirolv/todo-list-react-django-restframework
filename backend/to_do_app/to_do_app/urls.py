from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.custom_sessions import views
from apps.custom_sessions.auth import schema_view

from apps.to_do import views as view_to_do

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# APP to_do
router.register(r'projects', view_to_do.ProjectViewSet)
router.register(r'boards', view_to_do.BoardViewSet)
router.register(r'columns', view_to_do.ColumnViewSet)
router.register(r'tasks', view_to_do.TaskViewSet)
router.register(r'attachments', view_to_do.AttachmentViewSet)
router.register(r'checklists', view_to_do.ChecklistViewSet)
router.register(r'todo-items', view_to_do.ToDoItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin_secret/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
