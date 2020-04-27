from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from groupchat import groupchat_consumers
from privatechat import privatechat_consumers
import randomchat

application = ProtocolTypeRouter({

    # handler for websocket connections
    "websocket":URLRouter([
        path("groupchat/<str:room_name>/<str:username>/", groupchat_consumers.GroupChatConsumer),
        path("privatechat/", privatechat_consumers.PrivateChatConsumer),
        # path("randomchat/", randomchat.RandomChatConsumer)
    ])

    # handler for http connections getsautomatically added
})





# delete all the existing users on startup
from groupchat.models import User
list(map(User.delete, User.objects.all()))

# delete all the chat logs during server startup
from groupchat.models import Room
for r in Room.objects.all():
    r.messages = ""
    r.save()

