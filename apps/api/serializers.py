from rest_framework.serializers import ModelSerializer
from apps.info.models import CPUInfo


class CPUInfoSerializer(ModelSerializer):
    class Meta:
        model = CPUInfo
        fields = '__all__'
