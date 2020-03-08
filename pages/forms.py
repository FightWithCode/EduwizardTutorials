from django import forms
from .models import JoinQuery


class JoinQueryForm(forms.ModelForm):
    class Meta:
        model = JoinQuery
        fields = ('name', 'mobile_number', 'subject_or_class', 'message')
