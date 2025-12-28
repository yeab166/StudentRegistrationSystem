from django.contrib import admin
from django.urls import path, include
from routes.student_routes import urlpatterns as student_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(student_urls)),
]
