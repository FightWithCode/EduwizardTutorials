from django import forms
from pages.models import JoinQuery


class NotesQueryForm(forms.ModelForm):
    class Meta:
        model = JoinQuery
        fields = ('name', 'subject_or_class', 'message')
