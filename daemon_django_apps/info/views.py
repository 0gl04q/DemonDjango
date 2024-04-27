from django.shortcuts import render
from django.db.models import Min, Max, Avg
from daemon_django_apps.info.models import CPUInfo


def get_list_info_cpu(request):
    cpu_list_100 = CPUInfo.objects.all()[:100]

    min_max_avg_100 = cpu_list_100.aggregate(Min('cpu'), Max('cpu'), Avg('cpu'))
    min_max_avg_all = CPUInfo.objects.aggregate(Min('cpu'), Max('cpu'), Avg('cpu'))

    return render(request, 'info.html', context={
        'cpu_list': cpu_list_100,
        'min_max_avg_100': min_max_avg_100,
        'min_max_avg_all': min_max_avg_all
    })


def get_table(request):
    filter_table = request.GET.get('filter')
    direction = request.GET.get('direction')

    if filter_table:
        request.session['filter_table'] = filter_table
    else:
        filter_table = request.session['filter_table']

    if direction:
        request.session['direction'] = direction
    else:
        direction = request.session['direction']


    cpu_list_100 = CPUInfo.objects.all()[:100]

    min_max_avg_100 = cpu_list_100.aggregate(Min('cpu'), Max('cpu'), Avg('cpu'))
    min_max_avg_all = CPUInfo.objects.aggregate(Min('cpu'), Max('cpu'), Avg('cpu'))

    return render(request, 'table.html', context={
        'cpu_list': cpu_list_100,
        'min_max_avg_100': min_max_avg_100,
        'min_max_avg_all': min_max_avg_all
    })
