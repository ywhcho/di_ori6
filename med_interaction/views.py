from django.core.paginator import Paginator
from django.shortcuts import render

from medicines.models import Medicine

from .services import RISK_FILTER_OPTIONS, check_interactions


def interaction_check(request):
    """의약품 상호작용 보기"""
    query = request.GET.get('q', '').strip()
    selected_risk_filter = request.session.get('selected_interaction_risk_filter', '')
    search_results = Medicine.objects.none()
    search_page = None
    if query:
        search_results = (
            Medicine.objects.filter(htname__icontains=query)
            .values('htname')
            .distinct()
            .order_by('htname')
        )
        search_paginator = Paginator(search_results, 10)
        search_page_number = request.GET.get('qpage', 1)
        search_page = search_paginator.get_page(search_page_number)

    selected = request.session.get('selected_interaction_medicines', [])

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            name = request.POST.get('medicine_name', '').strip()
            if name and name not in selected:
                selected.append(name)
                request.session['selected_interaction_medicines'] = selected
        elif action == 'remove':
            name = request.POST.get('medicine_name', '').strip()
            if name in selected:
                selected.remove(name)
                request.session['selected_interaction_medicines'] = selected
        elif action == 'clear':
            selected = []
            request.session['selected_interaction_medicines'] = selected
        elif action == 'set_risk_filter':
            selected_risk_filter = request.POST.get('risk_filter', '').strip().upper()
            if selected_risk_filter not in {value for value, _ in RISK_FILTER_OPTIONS}:
                selected_risk_filter = ''
            request.session['selected_interaction_risk_filter'] = selected_risk_filter

    selected_paginator = Paginator(selected, 7)
    selected_page_number = request.GET.get('spage', 1)
    selected_page = selected_paginator.get_page(selected_page_number)

    interaction_result = None
    if request.method == 'POST' and request.POST.get('action') == 'check':
        selected = request.session.get('selected_interaction_medicines', [])
        selected_risk_filter = request.POST.get('risk_filter', '').strip().upper()
        if selected_risk_filter not in {value for value, _ in RISK_FILTER_OPTIONS}:
            selected_risk_filter = ''
        request.session['selected_interaction_risk_filter'] = selected_risk_filter
        interaction_result = check_interactions(selected, selected_risk_filter)

    context = {
        'query': query,
        'search_page': search_page,
        'selected_page': selected_page,
        'selected': selected,
        'interaction_result': interaction_result,
        'risk_filter_options': RISK_FILTER_OPTIONS,
        'selected_risk_filter': selected_risk_filter,
    }
    return render(request, 'med_interaction/interaction_check.html', context)
