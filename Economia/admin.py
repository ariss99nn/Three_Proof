
from django.contrib import admin
from .models import EconomicIndicator

@admin.register(EconomicIndicator)
class EconomicIndicatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'source', 'updated_at')
    search_fields = ('name',)