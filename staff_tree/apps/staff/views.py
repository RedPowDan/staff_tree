from datetime import datetime

from django.shortcuts import render

from .generator import Generator
from subdivisions.subdivision_services import get_tree_all_subdivisions


def tree(request):
    Generator.create_random_users()

    dict_tree_subdivisions = get_tree_all_subdivisions()

    start = datetime.now()
    rendered_http_response = render(request, 'staff/tree.html', {'dict_tree_subdivisions': dict_tree_subdivisions})
    ends = datetime.now()
    print(f'Time rendering html: {format(ends - start)}')
    return rendered_http_response
