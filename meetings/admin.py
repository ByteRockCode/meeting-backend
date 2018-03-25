from django.contrib import admin

from .forms import AgreementForm
from .forms import CompromiseForm
from .models import Agreement
from .models import Compromise
from .models import Guest
from .models import Meeting


class AgreementAdmin(admin.ModelAdmin):
    pass


class AgreementInline(admin.TabularInline):
    model = Agreement
    extra = 1
    form = AgreementForm


class CompromiseAdmin(admin.ModelAdmin):
    pass


class CompromiseInline(admin.TabularInline):
    model = Compromise
    extra = 1
    form = CompromiseForm


class GuestInline(admin.TabularInline):
    model = Guest
    extra = 1


class GuestAdmin(admin.ModelAdmin):
    pass


class MeetingAdmin(admin.ModelAdmin):
    inlines = (
        GuestInline,
        AgreementInline,
        CompromiseInline,
    )
    list_display = ('motive', 'get_companies_names')
    search_fields = ('motive', 'companies__name')
    labels_display = {
        'get_companies_names': 'companies',
    }

    def get_companies_names(self, obj):
        comapnies_names = list(obj.companies.order_by('name').values_list('name', flat=True))

        if len(comapnies_names) == 0:
            response = ''

        elif len(comapnies_names) == 1:
            response = comapnies_names[0]

        else:
            response = ', '.join(comapnies_names[:-1]) + ' y ' + comapnies_names[-1]

        return response


class GuestInline(admin.TabularInline):
    model = Guest
    extra = 1


admin.site.register(Agreement, AgreementAdmin)
admin.site.register(Compromise, CompromiseAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Meeting, MeetingAdmin)
