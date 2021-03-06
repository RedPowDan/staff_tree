# Generated by Django 3.1.2 on 2021-09-30 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер уровня')),
            ],
            options={
                'verbose_name': 'Уровень',
                'verbose_name_plural': 'Уровни',
            },
        ),
        migrations.CreateModel(
            name='PositionAtWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('second_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('employment_date', models.DateField(auto_now_add=True, verbose_name='Дата приёма на работу')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Зарплата')),
                ('level_in_subdivision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.level', verbose_name='Уровень в подразделении')),
                ('position_at_work', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff.positionatwork', verbose_name='Должность')),
                ('subdivision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.subdivision', verbose_name='Подразделение')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
    ]
