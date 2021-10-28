from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Thread,Comment
from .forms import ThreadForm,CommentForm
from django.views.generic import (TemplateView,ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)

# Create your views here.
class HomeView(TemplateView):
    template_name = 'newapp/home.html'


class ChelseaView(TemplateView):
    template_name = 'newapp/chelsea.html'


class InterView(TemplateView):
    template_name = 'newapp/inter.html'


class SpainView(TemplateView):
    template_name = 'newapp/spain.html'


class ThreadListView(ListView):
    model = Thread

    def get_queryset(self):
        return Thread.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')


class ThreadDetailView(DetailView):
    model = Thread


class ThreadCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_url_name = 'newapp/thread_detail.html'

    form_class = ThreadForm

    model = Thread


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_url_name = 'newapp/thread_detail.html'

    form_class = ThreadForm
    model = Thread


class ThreadDeleteView(LoginRequiredMixin,DeleteView):
    model = Thread
    success_url = reverse_lazy('thread_list')


### FUNCTIONS ###

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})


@login_required
def thread_create(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    thread.create()
    return redirect('thread_detail', pk=pk)


@login_required
def add_comment_to_thread(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.thread = thread
            comment.save()
            return redirect('thread_detail', pk= thread.pk)
    else:
        form = CommentForm()
        return render(request, 'newapp/comment_form.html', {'form': form})


@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('thread_detail', pk = comment.thread.pk)


@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    thread_pk = comment.thread.pk
    comment.delete()
    return redirect('thread_detail', pk = thread_pk)