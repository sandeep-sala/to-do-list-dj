from django.urls import path
from .views import *

urlpatterns = [
    path('', toToApp, name="todoApp"),
]
