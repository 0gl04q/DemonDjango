from django.urls import path

from daemon_django_apps.info.views import get_list_info_cpu, get_table

urlpatterns = [
    path('', get_list_info_cpu, name='list_info_cpu'),
    path('table/', get_table, name='table_info_cpu'),
    path('table/<str:filter_table>/<str:direction>', get_table, name='table_info_cpu_sort')
]
