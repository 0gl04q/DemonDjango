from rest_framework.serializers import ModelSerializer
from daemon_django_apps.info.models import CPUInfo


class CPUInfoSerializer(ModelSerializer):
    class Meta:
        model = CPUInfo
        fields = '__all__'
