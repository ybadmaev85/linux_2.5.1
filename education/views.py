from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from education.models import Сourse, Lesson, Subscription
from education.paginators import EducationPaginator
from education.permissions import IsModerator, IsMember, IsOwner
from education.serializers import СourseSerializer, LessonSerializer, SubscriptionSerializer
from tasks import subscription_mailing

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = СourseSerializer
    queryset = Сourse.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsModerator | IsMember]
    pagination_class = EducationPaginator

    def perform_create(self, serializer):
        new_instance = serializer.save()
        new_instance.user = self.request.user
        new_instance.save()

    def update(self, request, *args, **kwargs):
        course = self.get_object()
        subscription_mailing.delay(course.id, 'Course')
        return super().update(request, *args, **kwargs)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    # permission_classes = [IsAuthenticated, IsMember]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        lesson = serializer.save(owner=self.request.user)
        subscription_mailing.delay(lesson.id, 'Lesson')


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = EducationPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def update(self, request, *args, **kwargs):
        lesson = self.get_object()
        subscription_mailing.delay(lesson.id, 'Lesson')
        return super().update(request, *args, **kwargs)

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsOwner]


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [AllowAny]
