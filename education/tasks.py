from celery import shared_task
from django.core.mail import send_mail

from config import settings
from education.models import Subscription, Сourse, Lesson
from users.models import User


@shared_task
def subscription_mailing(pk, model):
    try:
        if model == "Course":
            print(pk)
            course = Сourse.objects.filter(pk=pk).first()
            print(course)
        else:
            print(pk)
            lesson = Lesson.objects.filter(pk=pk).first()
            print(lesson.course)
            course = lesson.course
            print(course)

        subscriptions = Subscription.objects.filter(is_active=True, course=course)
        print(subscriptions)
        users = []

        for subscription in subscriptions:
            users.append(subscription.user)

        for user in users:
            send_mail(
                subject='Информация по вашей подписке!',
                message=f'Обновлены материалы для курса {course.title}!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
        print(users)

    except Exception as e:
        print(f"Ошибка: {str(e)}")