from django.urls import path

from daemon_django_apps.api.views import CreateCPUInfoAPIView

urlpatterns = [
    path('', CreateCPUInfoAPIView.as_view(), name='create_cpu_info')
]
