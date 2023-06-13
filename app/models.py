from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    title = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, related_name='chat_messages', on_delete=models.CASCADE)
    content = models.TextField()
    time_send = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-time_send",)
