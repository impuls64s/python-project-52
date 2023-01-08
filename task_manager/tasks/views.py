from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Tasks
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
from django_filters.views import FilterView
from .filters import TaskFilter


# Класс который содержит все общие атрибуты классов CRUD
class TasksMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Tasks
    extra_context = {'title': ' New Tasks', 'button': 'Создать'}
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home_tasks')
    fields = ['name', 'description', 'status', 'executor', 'label']


class ListTasks(TasksMixin, FilterView):
    context_object_name = 'tasks'
    extra_context = {'title': 'Tasks'}
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter


class CreateTask(TasksMixin, CreateView):
    template_name = 'apps/apps_form.html'
    success_message = 'Задача создан, ебать ты молодец!'

    # Добавляем имя автора в поле author, которое не отображается в форме
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ViewTask(TasksMixin, DetailView):
    context_object_name = 'task'
    extra_context = {'title': 'Просмотр Задач'}


class UpdateTask(TasksMixin, UpdateView):
    template_name = 'apps/apps_form.html'
    extra_context = {'title': ' New Tasks', 'button': 'Изменить'}
    success_message = 'Задача изменена, ебать ты молодец!'


class DeleteTask(TasksMixin, DeleteView):
    template_name = 'apps/apps_confirm_delete.html'
    success_message = 'Задача успешно удалена'

    def has_permission(self) -> bool:
        return self.get_object().author.pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                self.request,
                "Error! You are not authenticated"
            )
            return self.handle_no_permission()

        elif not self.has_permission():
            messages.error(
                request,
                "Error! You can't delete this task. Only author"
            )
            return redirect('home_tasks')
        return super().dispatch(request, *args, **kwargs)
