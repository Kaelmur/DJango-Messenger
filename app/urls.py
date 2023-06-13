from django.urls import path
from .views import ChatsListView, ChatsDetailView, ChatCreateView, ChatUpdateView, ChatDeleteView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", ChatsListView.as_view(), name='w-home'),
    path("chat/<int:pk>/", login_required(ChatsDetailView.as_view()), name="chat-detail"),
    path('chat/new/', ChatCreateView.as_view(), name='chat-create'),
    path('chat/<int:pk>/update/', ChatUpdateView.as_view(), name='chat-update'),
    path('delete/<int:pk>/', ChatDeleteView.as_view(), name='chat-delete'),
]
