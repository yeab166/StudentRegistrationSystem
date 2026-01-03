from rest_framework import viewsets, generics
from .models import Student, Course, Enrollment
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer

# ----- ViewSets for CRUD -----
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# ----- Extra endpoints -----
class ListStudentEnrollments(generics.ListAPIView):
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        student_id = self.kwargs['pk']
        return Enrollment.objects.filter(student_id=student_id)

class ListCourseStudents(generics.ListAPIView):
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']
        return Enrollment.objects.filter(course_id=course_id)
