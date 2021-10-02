import random
from datetime import datetime

from django.contrib.auth.models import User
from subdivisions.models import PositionAtWork, Subdivision, Level

from staff.models import Employee
from staff_tree.generate_data.generators import (GeneratorPositionAtWork,
                                                 GeneratorSubdivision,
                                                 GeneratorLevels,
                                                 GeneratorRussianName,
                                                 GeneratorUsers)


class Generator:

    @staticmethod
    def create_users(count_users_in_db):
        start = datetime.now()
        generator_users = GeneratorUsers(count_models_in_db=count_users_in_db)
        generated_users = generator_users.generate()
        User.objects.bulk_create(generated_users)
        users = User.objects.filter(employee=None).filter(is_superuser=False)
        Generator.create_employee(users)
        ends = datetime.now()
        print(f'Time generation: {format(ends - start)}')

    @staticmethod
    def create_employee(users):
        employees = []

        Generator.create_dependencies_employee()

        position_at_work = PositionAtWork.objects.order_by('?')[0]
        subdivision = Subdivision.objects.order_by('?')[0]
        level_in_subdivision = Level.objects.order_by('?')[0]
        count_new_users = random.randint(1000, 2000)
        for index, user in enumerate(users):
            if index % count_new_users == 0:
                count_new_users = random.randint(1000, 2000)
                position_at_work = PositionAtWork.objects.order_by('?')[0]
                subdivision = Subdivision.objects.order_by('?')[0]
                level_in_subdivision = Level.objects.order_by('?')[0]
            employees.append(
                Employee(
                    first_name=f"full_name.first_name {index}",
                    second_name=f"full_name.second_name {index}",
                    last_name=f"full_name.last_name {index}",
                    position_at_work=position_at_work,
                    salary=random.randint(10000, 100000),
                    subdivision=subdivision,
                    level_in_subdivision=level_in_subdivision,
                    user=user
                )
            )
        Employee.objects.bulk_create(employees)

    @staticmethod
    def create_dependencies_employee():
        count_position_at_work_in_db = PositionAtWork.objects.count()
        count_subdivision_in_db = Subdivision.objects.count()
        count_level_in_db = Level.objects.count()

        Generator.create_positions_at_work(count_positions_at_work_in_db=count_position_at_work_in_db)
        Generator.create_subdivisions(count_subdivisions_in_db=count_subdivision_in_db)
        Generator.create_levels(count_level_in_db=count_level_in_db)

    @staticmethod
    def create_positions_at_work(count_positions_at_work_in_db):
        generator_positions = GeneratorPositionAtWork(count_models_in_db=count_positions_at_work_in_db)
        generated_positions_at_work = generator_positions.generate()
        if len(generated_positions_at_work) != 0:
            PositionAtWork.objects.bulk_create(generated_positions_at_work)

    @staticmethod
    def create_subdivisions(count_subdivisions_in_db):
        generator_subdivisions = GeneratorSubdivision(count_models_in_db=count_subdivisions_in_db)
        subdivision_models = generator_subdivisions.generate()
        if len(subdivision_models) != 0:
            Subdivision.objects.bulk_create(subdivision_models)

    @staticmethod
    def create_levels(count_level_in_db):
        generator_levels = GeneratorLevels(count_models_in_db=count_level_in_db)
        level_models = generator_levels.generate()
        if len(level_models) != 0:
            Level.objects.bulk_create(level_models)
