from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from education.models import Сourse, Lesson


class EducationTestCase(APITestCase):

    def setUp(self) -> None:
        self.course = Сourse.objects.create(
            title='test'
        )
        self.lesson = Lesson.objects.create(
            title='test',
            course=self.course
        )

    def test_get_list(self):
        """
        Тестирование просмотра уроков
        """

        response = self.client.get(
            reverse('education:lesson_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None,
             'results': [{'title': self.lesson.title, 'image': self.lesson.image, 'description': self.lesson.description,
                          'url': self.lesson.url, 'user': self.lesson.user_id, 'course': self.lesson.course_id}]}

        )

    def test_lesson_create(self):
        """
        Тест создания урока
        """

        data = {
            'title': 'test2',
            'course': self.course.id
        }

        response = self.client.post(
            reverse('education:lesson_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            Lesson.objects.all().count(),
            2
        )

    def test_lesson_create_validation_error(self):
        """
        Тест ошибки валидации
        """

        data = {
            'title': 'test3',
            'course': self.course.id,
            'url': 'сылочка'
        }

        response = self.client.post(
            reverse('education:lesson_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


class EducationTestCase2(APITestCase):
    """
    Тестирование апдейта
    """
    def setUp(self):
        self.lesson = Lesson.objects.create(
            title='test',
            description='test'
        )

    def test_lesson_update(self):
        url = reverse('education:lesson_update', kwargs={'pk': self.lesson.pk})

        data = {
            'title': self.lesson.title,
            'description': 'update_test'
        }

        response = self.client.put(url, data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {'title': 'test', 'image': None, 'description': 'update_test', 'url': None, 'user': None, 'course': None}

        )



    def test_lesson_delete(self):

        url = reverse('education:lesson_delete', kwargs={'pk': self.lesson.pk})

        response = self.client.delete(url)

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.all().exists(),
        )


class CreateSubscription(APITestCase):

    def create_user(self):
        self.user = User.objects.create(
            email='test@test.com',
            is_staff=False,
            is_active=True,
        )
        self.user.set_password('12345678')
        self.user.save()

    def setUp(self) -> None:
        self.create_user()
        self.data = {'user': self.user, 'is_active': True}

    def test_create_subscription(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(reverse('education-subscriptions'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

