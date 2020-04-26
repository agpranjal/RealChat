from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Rooms

def join_room(request):
    if request.method == "POST":
        username = request.POST["username"]
        room_name = request.POST["room_name"]

        # If room_name exists
        if room_name in list(map(str, Rooms.objects.all())):

            # If username does not exist already
            if username not in list(map(str, User.objects.all())):
                new_user = User.objects.create(username=username)
                return render(request, "groupchat/chat.html", {"username": username})
            else:
                return render(request, "groupchat/join_room.html", {"username_error":True})
        
        else:
            return render(request, "groupchat/join_room.html", {"room_error":True})
    
    # If page is accessed first time using GET
    return render(request, "groupchat/join_room.html", {"username_error":False})