from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Room, User
import json

class GroupChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        room_name = self.scope["url_route"]["kwargs"]["room_name"]

        # room_name room already exists
        # add the current channel layer to the group whose name is room_name
        async_to_sync(self.channel_layer.group_add)(room_name, self.channel_name)


        # send the existing messages to all the users in the room room_name
        # send the list of active users in the room_name room to everyone in the group
        r = Room.objects.get(room_name=room_name)
        messages = r.messages
        all_users = User.objects.filter(room__room_name = room_name)

        async_to_sync(self.channel_layer.group_send)(room_name, {
            "type": "groupchat.messages",
            "msg": messages,
            "all_users": list(map(str, all_users))
        })
    
    def disconnect(self, code):
        room_name = self.scope["url_route"]["kwargs"]["room_name"]
        username = self.scope["url_route"]["kwargs"]["username"]

        # delete the user from django.contrib.auth.models.User
        User.delete(User.objects.get(username=username))
        
        # remove the current channel layer from the group whose name is room_name
        async_to_sync(self.channel_layer.group_discard)(room_name, self.channel_name)
        self.close(code)
    
    def receive(self, text_data):
        room_name = self.scope["url_route"]["kwargs"]["room_name"]
        messages = json.loads(text_data)["messages"]
        
        # save the received messages in database
        room = Room.objects.get(room_name=room_name)
        room.messages += messages + "\n"
        room.save()

        # get the list of all active users
        all_users = User.objects.filter(room__room_name = room_name)

        async_to_sync(self.channel_layer.group_send)(room_name, {
            "type":"groupchat.messages",
            "msg": Room.objects.get(room_name=room_name).messages,
            "all_users": list(map(str, all_users))
        })
    
    def groupchat_messages(self, event):
        messages = event["msg"]
        all_users = event["all_users"]

        self.send(text_data=json.dumps({
            "messages":messages,
            "all_users":all_users
        }))