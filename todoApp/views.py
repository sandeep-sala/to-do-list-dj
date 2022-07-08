from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = "task_list"

class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("taskList")

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("taskList")

class TaskDelete(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("taskList")

taskList = TaskList.as_view()
taskDetail = TaskDetail.as_view()
taskCreate = TaskCreate.as_view()
taskUpdate = TaskUpdate.as_view()
taskDelete = TaskDelete.as_view()