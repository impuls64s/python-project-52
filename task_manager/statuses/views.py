from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Statuses
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.


# Класс который содержит все общие атрибуты классов CRUD
class StatusMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Statuses
    extra_context = {'title': 'Statuses', 'button': 'Создать'}
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('home_statuses')
    fields = ['name']


class ListStatuses(StatusMixin, ListView):
    context_object_name = 'statuses'


class CreateStatus(StatusMixin, CreateView):
    success_message = 'Статус создан, ебать ты молодец!'
    template_name = 'apps/apps_form.html'


class UpdateStatus(StatusMixin, UpdateView):
    success_message = 'Статус изменен, ебать ты молодец!'
    template_name = 'apps/apps_form.html'
    extra_context = {'title': 'Statuses', 'button': 'Изменить'}


class DeleteStatus(StatusMixin, DeleteView):
    success_message = 'Статус успешно удалён'
    template_name = 'apps/apps_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(
                self.request,
                'Status successfully deleted'
            )
            return redirect(reverse_lazy('home_statuses'))
        except ProtectedError:
            messages.error(
                self.request,
                "Error! Can't delete, status in use"
            )
            return redirect(reverse_lazy('home_statuses'))
