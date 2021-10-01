from django.contrib.auth.models import User
from django.shortcuts import render

from staff_tree.apps.staff.generator import Generator
from subdivisions.models import Subdivision, Level


def tree(request):
    count_users_in_db = User.objects.count()
    Generator.create_users(count_users_in_db=count_users_in_db)

    all_levels = Level.objects.all()

    dict_tree_employees = {}
    all_subdivisions = Subdivision.objects.all()
    for subdivision in all_subdivisions:
        employees_in_subdivision = subdivision.employee_set.all()

        dict_levels_and_employees = {}
        for level in all_levels:
            dict_levels_and_employees.update(
                {level: employees_in_subdivision.filter(level_in_subdivision=level).all()}
            )

        dict_tree_employees.update({subdivision: dict_levels_and_employees})

    return render(request, 'staff/tree.html', {'dict_tree_employees': dict_tree_employees})
