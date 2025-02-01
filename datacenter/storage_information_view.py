from django.shortcuts import render

from datacenter.func import format_duration, get_duration
from datacenter.models import Visit


def storage_information_view(request):
    non_closed_visits = []

    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append({
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': Visit.is_visit_long(visit)
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
