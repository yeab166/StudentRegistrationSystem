from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')
router.register('courses', views.CourseViewSet, basename='courses')
router.register('enrollments', views.EnrollmentViewSet, basename='enrollments')

urlpatterns = [
    path('', include(router.urls)),
    path('student/<int:pk>/enrollments/', views.ListStudentEnrollments.as_view(), name='student-enrollments'),
    path('course/<int:pk>/enrollments/', views.ListCourseStudents.as_view(), name='course-students'),
]
