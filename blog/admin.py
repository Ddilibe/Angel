from django.contrib import admin
from .models import Audit

@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','gender','phone_number')
    search_fields = ('first_name', 'last_name','list_any_talent_or_performing_experience')
    date_hierarchy = 'created'
    ordering = ('created', 'first_name')
