from django.shortcuts import render
from django.http import HttpResponse

def join_chat(request):
    username = request.user.username
    return render(request, "privatechat/join_chat.html")
