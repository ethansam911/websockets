from channels.routing import ProtocolTypeRouter, URLRouter 
from django.urls import path 

# from notifier.consumers import EchoConsumer
# from notifier.consumers import TickTockConsumer
from notifier.consumers import NoseyConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        # path("ws/", EchoConsumer),
        #  path("ws/", TickTockConsumer),
        path("notifications/", NoseyConsumer),
    ])
})
