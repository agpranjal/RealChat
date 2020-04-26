from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from groupchat import groupchat_consumers
import privatechat
import randomchat

application = ProtocolTypeRouter({

    # handler for websocket connections
    "websocket":URLRouter([
        path("groupchat/<str:room_name>/", groupchat_consumers.GroupChatConsumer),
        # path("privatechat/", privatechat.PrivateChatConsumer),
        # path("randomchat/", randomchat.RandomChatConsumer)
    ])

    # handler for http connections getsautomatically added
})