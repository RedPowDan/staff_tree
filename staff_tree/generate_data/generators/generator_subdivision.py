from staff_tree.generate_data.generators.base_generator import BaseGenerator

from subdivisions.models import Subdivision


class GeneratorSubdivision(BaseGenerator):
    MAX_COUNT_IN_DATABASE = 25

    def __init__(self, count_models_in_db):
        self.count_models_in_db = count_models_in_db

    def generate(self):
        count_models_in_db = self._get_count_models_in_db()
        subdivisions = []
        if count_models_in_db < self.MAX_COUNT_IN_DATABASE:
            subdivisions = [Subdivision(name=name)
                            for name in self._get_list_names_subdivisions()]
        return subdivisions

    def _get_count_models_in_db(self):
        return self.count_models_in_db

    def _get_list_names_subdivisions(self):
        names = []
        for i in range(self.count_models_in_db, self.MAX_COUNT_IN_DATABASE):
            names.append(f"Подразделение №{i + 1}")
        return names
