from staff_tree.generate_data.generators.base_generator import BaseGenerator

from subdivisions.models import Level


class GeneratorLevels(BaseGenerator):
    """Генератор уровней по модели Level для пользователей"""
    MAX_COUNT_IN_DATABASE = 5

    def __init__(self, count_models_in_db):
        self.count_models_in_db = count_models_in_db

    def generate(self):
        count_models_in_db = self._get_count_models_in_db()
        levels = []
        if count_models_in_db < self.MAX_COUNT_IN_DATABASE:
            levels = [Level(number=number)
                      for number in self._get_list_numbers_level()]
        return levels

    def _get_count_models_in_db(self):
        return self.count_models_in_db

    def _get_list_numbers_level(self):
        names = []
        for i in range(self.count_models_in_db, self.MAX_COUNT_IN_DATABASE):
            names.append(i + 1)
        return names
