from django import forms
from .models import JoinQuery, NewsLetter


class JoinQueryForm(forms.ModelForm):
    class Meta:
        model = JoinQuery
        fields = ('name', 'mobile_number', 'subject_or_class', 'message')


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('email',)
