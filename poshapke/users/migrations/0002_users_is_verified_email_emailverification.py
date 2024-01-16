# Generated by Django 4.2.8 on 2024-01-16 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_verified_email',
            field=models.BooleanField(default=False, verbose_name='Подтверждение Почты'),
        ),
        migrations.CreateModel(
            name='EmailVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_uuid', models.UUIDField(unique=True, verbose_name='Уникальная ссылка')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время Создания')),
                ('expiration', models.DateTimeField(verbose_name='Истечение срока действия')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Новый Пользователь')),
            ],
            options={
                'verbose_name': 'Подтверждение Почты',
                'verbose_name_plural': 'Подтверждение Почты',
            },
        ),
    ]