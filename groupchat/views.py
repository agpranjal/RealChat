from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Room

def join_room(request):
    all_rooms = list(map(str, Room.objects.all()))

    if request.method == "POST":
        username = request.POST["username"]
        room_name = request.POST["room_name"]

        # If room_name exists
        if room_name in list(map(str, Room.objects.all())):

            # get the room_name object
            r = Room.objects.get(room_name=room_name)

            # If username does not exist already
            if username not in list(map(str, User.objects.all())):
                new_user = User.objects.create(username=username, room=r)
                return render(request, "groupchat/chat.html", {
                    "username": username,
                    "room_name": room_name,
                })
            
            # If username already exists
            else:
                return render(request, "groupchat/join_room.html", {
                    "username_error":True,
                    "all_rooms":all_rooms
                    })
        
        # If room_name does not exist
        else:
            return render(request, "groupchat/join_room.html", {
                "room_error":True,
                "all_rooms":all_rooms
                })
    

    # If page is accessed first time using GET
    return render(request, "groupchat/join_room.html", {
        "username_error":False,
        "all_rooms":all_rooms
        })