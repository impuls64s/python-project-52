import django_filters
from task_manager.labels.models import Labels
from task_manager.tasks.models import Tasks
from django import forms


class TaskFilter(django_filters.FilterSet):
    def show_own_task(self, queryset, arg, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
    
    own_tasks = django_filters.BooleanFilter(
        method='show_own_task',
        widget=forms.CheckboxInput,
        label='Show own tasks',
    )
    label = django_filters.ModelChoiceFilter(
        queryset=Labels.objects.all(),
        label='Label',
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )
    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'label']
