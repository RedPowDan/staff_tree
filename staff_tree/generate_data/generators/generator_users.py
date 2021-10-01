from django.contrib.auth.models import User

from staff_tree.generate_data.generators import BaseGenerator


class GeneratorUsers(BaseGenerator):
    MAX_COUNT_IN_DATABASE = 50000

    def __init__(self, count_models_in_db):
        self.count_models_in_db = count_models_in_db

    def generate(self):
        users = [User(username=i, password=f"{i}super-super")
                 for i in range(self.count_models_in_db, self.MAX_COUNT_IN_DATABASE)]
        return users
