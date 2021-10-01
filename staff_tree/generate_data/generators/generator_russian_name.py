from russian_names import RussianNames

from staff_tree.generate_data.generators.base_generator import BaseGenerator


class FullName:
    def __init__(self, first_name, second_name, last_name):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name


class GeneratorRussianName(BaseGenerator):
    def generate(self):
        return self._get_random_full_name()

    @staticmethod
    def _get_random_full_name():
        full_name = RussianNames(count=1, output_type='dict').get_batch()[0]
        first_name = full_name['name']
        second_name = full_name['patronymic']
        last_name = full_name['surname']
        return FullName(first_name, second_name, last_name)
