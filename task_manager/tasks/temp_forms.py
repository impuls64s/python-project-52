from django import forms
from .models import Tasks


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            'name',
            'description',
            'status',
            'author',
            'executor',
        ]
        widgets = {'author': forms.HiddenInput(),}
