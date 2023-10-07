from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from education.models import Сourse, Lesson
from education.permissions import IsModerator
from education.serializers import СourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = СourseSerializer
    queryset = Сourse.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()