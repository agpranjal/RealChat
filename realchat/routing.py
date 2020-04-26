from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from .. import groupchat
from .. import privatechat
from .. import randomchat

application = ProtocolTypeRouter({
    "websocket":URLRouter([
        path("groupchat/", groupchat.GroupChatConsumer),
        path("privatechat/", privatechat.PrivateChatConsumer),
        path("randomchat/", randomchat.RandomChatConsumer)
    ])
})