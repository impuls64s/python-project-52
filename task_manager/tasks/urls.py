from django.urls import path
from .views import ListTasks , CreateTask, UpdateTask, DeleteTask, ViewTask

from django_filters.views import FilterView
from .models import Tasks

urlpatterns = [
    path('', ListTasks.as_view(), name='home_tasks'),
    #path('', FilterView.as_view(model=Tasks, template_name='tasks/tasks_list.html'), name='home_tasks'),
    path('<int:pk>/', ViewTask.as_view(), name='view_task'),
    path('create/', CreateTask.as_view(), name='create_task'),
    path('<int:pk>/update/', UpdateTask.as_view(), name='update_task'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete_task'),
]
