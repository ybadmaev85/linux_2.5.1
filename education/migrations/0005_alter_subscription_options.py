# Generated by Django 4.2.5 on 2023-10-12 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_subscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'подписка', 'verbose_name_plural': 'подписки'},
        ),
    ]
