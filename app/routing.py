from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/(?P<room_name>\d+)/$', consumers.ChatConsumer.as_asgi())
]
