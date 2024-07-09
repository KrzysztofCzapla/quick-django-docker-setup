imports = """from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions"""

schema_view = '''
schema_view = get_schema_view(
    openapi.Info(
        title="College Enrolment System",
        default_version="v0.1",
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)'''

swagger_path = '''    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),'''