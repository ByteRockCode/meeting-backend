from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        exclude = (
            'slug',
        )
        model = Company
