from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.db.models import Sum
from .models import DrugInfo
from .models import Medicine


# ---------- 의약정보 보기 ----------

def druginfo_list(request):
    """의약정보 목록 - 분야 선택 + 검색어로 검색"""
    field_map = {
        'htname': ('htname', '약품명'),
        'ingr_t': ('ingr_t', '성분명'),
        'company': ('company', '회사'),
        'ee': ('ee', '효능'),
    }
    search_field = request.GET.get('field', 'htname').strip()
    search_q = request.GET.get('q', '').strip()
    if search_field not in field_map:
        search_field = 'htname'

    ##drugs = DrugInfo.objects.all()
    medicines = Medicine.objects.all()

    if search_q:
        filter_field = field_map[search_field][0]
        medicines = medicines.filter(**{f'{filter_field}__icontains': search_q})

    ypri24_total = medicines.aggregate(total=Sum('ypri24'))['total'] or 0

    paginator = Paginator(medicines, 10)
    page_number = request.GET.get('page', 1) if search_q else 1
    page_obj = paginator.get_page(page_number)
    show_pagination = bool(search_q) and page_obj.has_other_pages()

    context = {
        'page_obj': page_obj,
        'show_pagination': show_pagination,
        'search_field': search_field,
        'search_field_label': field_map[search_field][1],
        'search_q': search_q,
        'ypri24_total': ypri24_total,
    }
    return render(request, 'medicines/druginfo_list.html', context)


def druginfo_detail(request, pk):
    """의약정보 상세 보기"""
    drug = get_object_or_404(DrugInfo, pk=pk)
    return render(request, 'medicines/druginfo_detail.html', {'drug': drug})
