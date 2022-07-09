from django.views.generic import FormView, ListView, CreateView, UpdateView
from django.views.generic.edit import *
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .models import Task
from django.utils import timezone

class TaskLogin(LoginView):
    template_name = 'todoApp/login.html'
    next_page = reverse_lazy("taskList")

class TaskLogout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy("taskList")

class TaskRegister(FormView):
    template_name = 'todoApp/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("taskList")

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(TaskRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super(TaskRegister, self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin, ListView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(user=self.request.user)
        context['count'] = context['task_list'].filter(complete=False).count()
        context['today_date'] = timezone.localtime()
        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context['task_list'] = context['task_list'].filter(
                title__icontains=search_input)
            context['search_input'] = search_input
        return context

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "todoApp/task_create.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("taskList")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "todoApp/task_update.html"
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("taskList")


def taskDelete(request, pk):
    try:
        Task.objects.get(user=request.user,pk=pk).delete()
    except:
        pass
    return HttpResponseRedirect(reverse_lazy("taskList"))

def taskDeleteAll(request):
    Task.objects.filter(user=request.user).delete()
    return HttpResponseRedirect(reverse_lazy("taskList"))

def completeTask(request, id, value):
    try:
        task_obj = Task.objects.get(user=request.user,pk=id)
        task_obj.complete = value
        task_obj.save()
    except:
        pass
    return HttpResponseRedirect(reverse_lazy("taskList"))


taskLogin = TaskLogin.as_view()
taskLogout = TaskLogout.as_view()
taskRegister = TaskRegister.as_view()
taskList = TaskList.as_view()
taskCreate = TaskCreate.as_view()
taskUpdate = TaskUpdate.as_view()
