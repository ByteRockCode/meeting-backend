from django import forms

from .models import Agreement
from .models import Compromise


class AgreementForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = Agreement


class CompromiseForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        model = Compromise
