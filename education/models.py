from django.db import models

from users.models import User


class Сourse(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    image = models.ImageField(upload_to='courses/', verbose_name='картинка')
    description = models.TextField(max_length=450, verbose_name='описание')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    image = models.ImageField(upload_to='lessons/', verbose_name='картинка')
    description = models.TextField(max_length=450, verbose_name='описание')
    url = models.URLField(verbose_name='ссылка')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Сourse, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Сourse, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='подписка')

    def __str__(self):
        return f'{self.is_active}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'