from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Room
import json

class GroupChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        room_name = self.scope["url_route"]["kwargs"]["room_name"]

        # send the existing messages to the newly connected client
        r = Room.objects.get(room_name=room_name)
        self.send(text_data=json.dumps({"messages":r.messages}))

        # room_name room already exists
        # add the current channel layer to the group whose name is room_name
        async_to_sync(self.channel_layer.group_add)(room_name, self.channel_name)
    
    def disconnect(self, code):
        room_name = self.scope["url_route"]["kwargs"]["room_name"]
        
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


        async_to_sync(self.channel_layer.group_send)(room_name, {
            "type":"groupchat.messages",
            "msg": Room.objects.get(room_name=room_name).messages
        })
    
    def groupchat_messages(self, event):
        messages = event["msg"]
        self.send(text_data=json.dumps({"messages":messages}))