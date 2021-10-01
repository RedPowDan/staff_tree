from django.contrib.auth.models import User
from django.shortcuts import render

from staff_tree.apps.staff.generator import Generator
from staff.models import Employee


def tree(request):
    count_users_in_db = User.objects.count()
    Generator.create_users(count_users_in_db=count_users_in_db)

    all_employees = Employee.objects.all()

    return render(request, 'staff/tree.html', {'all_employees': all_employees})
