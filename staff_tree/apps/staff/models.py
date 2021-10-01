from django.contrib.auth.models import User
from django.db import models

from subdivisions.models import PositionAtWork, Subdivision, Level


class Employee(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    first_name = models.CharField(
        verbose_name="Имя",
        max_length=30
    )

    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=30
    )

    second_name = models.CharField(
        verbose_name="Отчество",
        max_length=30
    )

    position_at_work = models.ForeignKey(
        to=PositionAtWork,
        verbose_name="Должность",
        on_delete=models.PROTECT
    )

    employment_date = models.DateField(
        verbose_name="Дата приёма на работу",
        auto_now_add=True
    )

    salary = models.DecimalField(
        verbose_name="Зарплата",
        max_digits=10,
        decimal_places=2
    )

    subdivision = models.ForeignKey(
        to=Subdivision,
        verbose_name="Подразделение",
        on_delete=models.CASCADE
    )

    level_in_subdivision = models.ForeignKey(
        to=Level,
        verbose_name="Уровень в подразделении",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name[:1]}.{self.second_name[:1]}"

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
