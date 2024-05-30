from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="To-Do API",
        default_version='v1',
        description="API documentation for the To-Do application",
    ),
    public=True,
    permission_classes=(AllowAny,),
)