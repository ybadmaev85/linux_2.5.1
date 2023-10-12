from rest_framework import serializers

from education.models import Сourse, Lesson, Subscription
from education.validators import UrlValidator


class LessonAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'pk',
            'title',
        )


class СourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonAllSerializer(source='lesson_set', many=True)
    validators = []

    class Meta:
        model = Сourse
        fields = (
            'pk',
            'title',
            'description',
            'lesson_count',
            'lessons'
        )
        UrlValidator = [UrlValidator(field='description')]

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('title', 'image', 'description', 'url',)
        UrlValidator = [UrlValidator(field='url')]


class SubscriptionSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для модели подписки
    '''

    class Meta:
        model = Subscription
        fields = (
            'user',
            'course',
            'is_active',
        )
