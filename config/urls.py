from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.messages import api
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("accounts.urls"), name="accounts"),
    path("api/projects/", include("projects.urls"), name="projects"),
    path("api/comments/", include("comments.urls"), name="comments"),
    path("api/tasks/", include("tasks.urls"), name="tasks"),
]

if settings.DEBUG:
    urlpatterns += [
        # YOUR PATTERNS
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        # Optional UI:
        path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
