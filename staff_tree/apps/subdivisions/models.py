from django.db import models


class Level(models.Model):
    number = models.IntegerField(
        verbose_name="Номер уровня"
    )

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

    def __str__(self):
        return f"Уровень {self.number}"


class PositionAtWork(models.Model):

    name = models.CharField(
        verbose_name="Название",
        max_length=40
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Subdivision(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

