from rest_framework.generics import CreateAPIView

from daemon_django_apps.api.serializers import CPUInfoSerializer
from daemon_django_apps.info.models import CPUInfo


class CreateCPUInfoAPIView(CreateAPIView):
    queryset = CPUInfo.objects.all()
    serializer_class = CPUInfoSerializer

