from django.urls import path

from daemon_django_apps.info.views import get_list_info_cpu

urlpatterns = [
    path('', get_list_info_cpu, name='list_info_cpu')
]
