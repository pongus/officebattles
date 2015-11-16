from django import forms
from .models import Company, Logo


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']


class LogoForm(forms.ModelForm):
    class Meta:
        model = Logo
        fields = ['logo']
