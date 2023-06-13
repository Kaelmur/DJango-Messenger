from django.shortcuts import render, get_object_or_404
from .models import Message, Chat
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages


class ChatsListView(ListView):
    model = Chat
    template_name = 'app/index.html'
    context_object_name = 'Chats'
    paginate_by = 9


class ChatsDetailView(DetailView):
    model = Chat


class ChatCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Chat
    fields = ['title']
    success_url = "/"

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        if self.test_func():
            messages.success(self.request, "Chat Created Successfully!")
            return super().form_valid(form)


class ChatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chat
    fields = ["title"]
    success_url = "/"
    extra_context = {'update': True}

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        if self.test_func():
            messages.success(self.request, "Chat Updated!")
            return super().form_valid(form)


class ChatDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chat
    success_url = '/'
    template_name = 'app/chat_confirm_delete.html'


    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        if self.test_func():
            messages.success(self.request, "Chat Deleted Successfully!")
            return super().form_valid(form)
