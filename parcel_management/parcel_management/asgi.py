# # asgi.py

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from parcels.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parcel_management.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # This handles the standard HTTP requests.
    "websocket": AuthMiddlewareStack(  # This handles WebSocket requests.
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
