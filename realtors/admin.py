from django.contrib import admin
from .models import Realtor
# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',
    'hire_date', 'is_mvp', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
    list_editable = ('is_mvp',)

admin.site.register(Realtor, RealtorAdmin)