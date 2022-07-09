from django.urls import path
from .views import *

urlpatterns = [
    path('', taskList, name="taskList"),
    path('login/', taskLogin, name="taskLogin"),
    path('register/', taskRegister, name="taskRegister"),
    path('logout/', taskLogout, name="taskLogout"),
    path('task-create/', taskCreate, name="taskCreate"),
    path('task-update/<int:pk>/', taskUpdate, name="taskUpdate"),
    path('task-delete/<int:pk>/', taskDelete, name="taskDelete"),
    path('task-delete-all/', taskDeleteAll, name="taskDeleteAll"),
    path('task-complete/<int:id>/<int:value>/', completeTask, name="completeTask"),
]
