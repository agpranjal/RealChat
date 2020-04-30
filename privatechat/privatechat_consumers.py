from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from .models import Messages
import json

# mapping between username and channel name
# aka list of online users
active_users = {}

class PrivateChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

        username = self.scope["url_route"]["kwargs"]["username"]
        destination_username = self.scope["url_route"]["kwargs"]["destination_username"]
        
        # add the current user to active_users
        active_users[username] = self.channel_name

        # send the chat log between source user(username) and destination_username to source user(username)
        user= User.objects.get(username=username)
        x = user.messages_set.get(message_from=destination_username)
        self.send(text_data=json.dumps({
            "message":x.message,
            "reset":True,
            }))

    def disconnect(self, code):

            # remove the current user from active_users
        username = self.scope["url_route"]["kwargs"]["username"]
        del active_users[username]
        self.close()


    def receive(self, text_data):

        username = self.scope["url_route"]["kwargs"]["username"]
        destination_username = self.scope["url_route"]["kwargs"]["destination_username"]

        message = json.loads(text_data)["message"] + "\n";

        # echo the message back to the source user
        # so that he can see what he just sent
        self.send(text_data=json.dumps({
            "message":message,
            "from_user":destination_username
            }))


        # send message to the destination_username
        # thru its channel_name in active_users
        # ONLY IF the user in online .. otherwise skip this step
        if destination_username in active_users:
            async_to_sync(self.channel_layer.send)(active_users[destination_username], {
                "type":"send.message",
                "message":message,
                "reset":False,
                "from_user":username
                })

        # add the message to the source user database
        u = User.objects.get(username=username)
        x = u.messages_set.get(message_from=destination_username)
        x.message += message
        x.save()

        # add the message to the destination users database
        u = User.objects.get(username=destination_username)
        x = u.messages_set.get(message_from=username)
        x.message += message
        x.save()



    def send_message(self, event):
        message = event["message"]
        reset = event["reset"]
        from_user = event["from_user"]

        self.send(text_data=json.dumps({
          "message":message,
          "reset":reset,
          "from_user":from_user
        }))
