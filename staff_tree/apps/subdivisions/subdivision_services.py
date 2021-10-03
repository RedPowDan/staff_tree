from .models import Subdivision, Level


def get_tree_all_subdivisions() -> dict:
    """Выводит дерево подразделений в которых содержатся уровни, в уровнях сотрудники"""
    all_levels = Level.objects.all()

    dict_tree_subdivisions = {}
    all_subdivisions = Subdivision.objects.all()
    for subdivision in all_subdivisions:
        employees_in_subdivision = subdivision.employee_set.all()

        dict_levels_and_employees = {}
        for level in all_levels:
            dict_levels_and_employees.update(
                {level: employees_in_subdivision.filter(level_in_subdivision=level)}
            )

        dict_tree_subdivisions.update({subdivision: dict_levels_and_employees})

    return dict_tree_subdivisions
