from django.urls import path

from  task_manager.users import views
from .views import SignUp


urlpatterns = [
    path('', views.index),
    path('create/', SignUp.as_view(), name = 'create_user'),
]