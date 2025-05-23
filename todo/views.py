from django.shortcuts import render, redirect
from blog.models import Todo
from .forms import TodoForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

# Create your views here.


def todo_list_fbv(request):
    todos = Todo.objects.all()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-fbv')
    else:
        form = TodoForm()

    return render(request, 'blog/todo_fbv.html', {'form': form, 'todos': todos})

class TodoListCBV(CreateView, ListView):
    model = Todo
    form_class = TodoForm
    template_name = 'blog/todo_cbv.html'
    success_url = reverse_lazy('todo-cbv')
    context_object_name = 'todos'