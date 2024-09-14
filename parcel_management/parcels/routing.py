from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/parcel/(?P<tracking_number>\w+)/$', consumers.ParcelConsumer.as_asgi()),
]