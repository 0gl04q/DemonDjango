from rest_framework.generics import CreateAPIView

from apps.api.serializers import CPUInfoSerializer
from apps.info.models import CPUInfo


class CreateCPUInfoAPIView(CreateAPIView):
    queryset = CPUInfo.objects.all()
    serializer_class = CPUInfoSerializer

