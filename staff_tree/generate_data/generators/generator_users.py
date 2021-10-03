from django.contrib.auth.models import User

from staff_tree.generate_data.generators import BaseGenerator

import random
import string


class GeneratorUsers(BaseGenerator):
    """Генертор пользователей по модели User"""
    MAX_COUNT_IN_DATABASE = 50000

    def __init__(self, count_models_in_db):
        self.count_models_in_db = count_models_in_db

    def generate(self):
        users = [User(username=self._generate_random_string(10) + "_" + str(i), password=f"{i}super-super")
                 for i in range(self.count_models_in_db, self.MAX_COUNT_IN_DATABASE)]
        return users

    @staticmethod
    def _generate_random_string(length) -> str:
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string
