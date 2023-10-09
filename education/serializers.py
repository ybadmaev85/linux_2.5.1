from rest_framework import serializers

from education.models import Сourse, Lesson


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

    class Meta:
        model = Сourse
        fields = (
            'pk',
            'title',
            'description',
            'lesson_count',
            'lessons'
        )

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('title', 'image', 'description', 'url',)
