from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from .forms import UsersForm

# Create your views here.
def index(request):
    return HttpResponse('This Users')


class SignUp(CreateView):
    form_class = UsersForm
    success_url = reverse_lazy("index")
    template_name = "users/registration.html"
