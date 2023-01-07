from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Вход в систему и вывод флеш сообщения
class SignIn(SuccessMessageMixin, LoginView):
    template_name ='login.html'
    success_message = 'Successfully login'

# Выход из системы и вывод флеш сообщения
class LogOut(SuccessMessageMixin, LogoutView):
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Successfully logged out.')
        return response
