from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # All API routes under /api/
    path('api/', include('school.urls')),

    # Django admin
    path('admin/', admin.site.urls),
]
