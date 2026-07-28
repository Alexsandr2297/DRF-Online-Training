from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from materials.models import Lesson, Course
from materials.serializers import LessonSerializer, CourseSerializer


class CourseViewSet(ModelViewSet):
    """CRUD для курсов через ViewSet"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonCreateAPIView(CreateAPIView):
    """Создание урока"""
    serializer_class = CourseSerializer


class LessonListApiView(ListAPIView):
    """Список уроков"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    """Получение одного урока"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonUpdateAPIView(UpdateAPIView):
    """Обновление урока"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonDestroyAPIView(DestroyAPIView):
    """Удаление урока"""
    serializer_class = CourseSerializer