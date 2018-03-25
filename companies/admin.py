from django.contrib import admin

from .forms import CompanyForm
from .models import Company


class CompanyAdmin(admin.ModelAdmin):

    form = CompanyForm
    list_display = ('name', 'slug')
    search_fields = ('name', 'description')


admin.site.register(Company, CompanyAdmin)
