from django.contrib import admin
from .models import Medicine, DrugInfo


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('htname', 'ingr_t', 'company')
    search_fields = ('htname', 'ingr_t', 'company')


@admin.register(DrugInfo)
class DrugInfoAdmin(admin.ModelAdmin):
    list_display = ('htname', 'ingr_t', 'company')
    search_fields = ('htname', 'ingr_t', 'company')
