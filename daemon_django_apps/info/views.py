from django.shortcuts import render

from daemon_django_apps.info.models import CPUInfo


def get_list_info_cpu(request):
    cpu_list = CPUInfo.objects.all()[:100]
    return render(request, 'info.html', context={'cpu_list': cpu_list})
