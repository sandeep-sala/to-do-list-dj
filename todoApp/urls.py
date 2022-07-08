from django.urls import path
from .views import taskList, taskDetail, taskCreate, taskUpdate, taskDelete

urlpatterns = [
    path('', taskList, name="taskList"),
    path('task/<int:pk>/', taskDetail, name="taskDetail"),
    path('task-create/', taskCreate, name="taskCreate"),
    path('task-update/<int:pk>/', taskUpdate, name="taskUpdate"),
    path('task-delete/<int:pk>/', taskDelete, name="taskDelete"),
]
