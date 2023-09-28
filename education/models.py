from django.db import models


class Сourse(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    image = models.ImageField(upload_to='courses/', verbose_name='картинка')
    description = models.TextField(max_length=450, verbose_name='описание')

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

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'