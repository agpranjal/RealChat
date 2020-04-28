from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def chat(request):

    return render(request, "privatechat/chat.html",{
        "active_users":list(map(str, User.objects.all()))
        })
