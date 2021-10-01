import random

from django.db import transaction

from subdivisions.models import PositionAtWork
from staff_tree.generate_data.generators.base_generator import BaseGenerator


class GeneratorPositionAtWork(BaseGenerator):
    MAX_COUNT_IN_DATABASE = 5

    def __init__(self, count_models_in_db):
        self.count_models_in_db = count_models_in_db

    NAMES_POSITION_AT_WORK = [
        'Старший специалист',
        'Младший специалист',
        'Стажёр',
        'Менеджер',
        'Разнорабочий'
    ]

    def generate(self):
        if self._get_count_models_in_db() < self.MAX_COUNT_IN_DATABASE:
            return [PositionAtWork(name=name)
                    for name in self.NAMES_POSITION_AT_WORK]
        return []

    def _get_count_models_in_db(self):
        return self.count_models_in_db
