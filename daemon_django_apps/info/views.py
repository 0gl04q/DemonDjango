from django.shortcuts import render
from django.db.models import Min, Max, Avg
from daemon_django_apps.info.models import CPUInfo


def get_list_info_cpu(request):
    request.session['filter_table'] = None
    request.session['direction'] = None

    cpu_list_100 = CPUInfo.objects.all()[:100]

    min_max_avg_100 = cpu_list_100.aggregate(Min('cpu'), Max('cpu'), Avg('cpu'))
    min_max_avg_all = CPUInfo.objects.aggregate(Min('cpu'), Max('cpu'), Avg('cpu'))

    return render(request, 'info.html', context={
        'cpu_list': cpu_list_100,
        'min_max_avg_100': min_max_avg_100,
        'min_max_avg_all': min_max_avg_all
    })


def get_table(request, filter_table="Undefined", direction="Undefined"):
    filter_session = request.session['filter_table']
    direction_session = request.session['filter_table']

    if filter_table != "Undefined":
        request.session['filter_table'] = filter_table
        cpu_list_100 = CPUInfo.objects.order_by(f'{"" if direction == "ascend" else "-"}{filter_table}')[:100]
    elif filter_session:
        cpu_list_100 = CPUInfo.objects.order_by(f'{"" if direction_session == "ascend" else "-"}{filter_session}')[:100]
    else:
        cpu_list_100 = CPUInfo.objects.all()[:100]

    min_max_avg_100 = cpu_list_100.aggregate(Min('cpu'), Max('cpu'), Avg('cpu'))
    min_max_avg_all = CPUInfo.objects.aggregate(Min('cpu'), Max('cpu'), Avg('cpu'))

    return render(request, 'table.html', context={
        'cpu_list': cpu_list_100,
        'min_max_avg_100': min_max_avg_100,
        'min_max_avg_all': min_max_avg_all
    })
