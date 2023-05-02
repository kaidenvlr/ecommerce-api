from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('api/store/', include('store.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns += [
    path('docs/', TemplateView.as_view(
        template_name='swagger/template.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]

urlpatterns += [
    # ...
    # Use the `get_schema_view()` helper to add a `SchemaView` to project URLs.
    #   * `title` and `description` parameters are passed to `SchemaGenerator`.
    #   * Provide view name for use with `reverse()`.
    path('redoc/', get_schema_view(
        title="E-Commerce",
        description="Developed by kaidenvlr",
        version="0.0.1"
    ), name='openapi-schema'),
    # ...
]
