from django.urls import path
from controllers.student_controller import StudentAPI

urlpatterns = [
    path('students/', StudentAPI.as_view()),
]
