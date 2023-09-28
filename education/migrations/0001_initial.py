# Generated by Django 4.2.5 on 2023-09-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='название')),
                ('image', models.ImageField(upload_to='lessons/', verbose_name='картинка')),
                ('description', models.TextField(max_length=450, verbose_name='описание')),
                ('url', models.URLField(verbose_name='ссылка')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
        migrations.CreateModel(
            name='Сourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='название')),
                ('image', models.ImageField(upload_to='courses/', verbose_name='картинка')),
                ('description', models.TextField(max_length=450, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
    ]
