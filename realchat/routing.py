from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from groupchat import groupchat_consumers
from privatechat import privatechat_consumers

application = ProtocolTypeRouter({

    # handler for websocket connections
    "websocket":URLRouter([
        path("groupchat/<str:room_name>/<str:username>/", groupchat_consumers.GroupChatConsumer),
        path("privatechat/<str:username>/<str:destination_username>/", privatechat_consumers.PrivateChatConsumer)
    ])

    # handler for http connections getsautomatically added
})

# Remove all the existing Users from groupchat.models.User
# (result of a bug)
from groupchat.models import User
list(map(User.delete, User.objects.all()))
