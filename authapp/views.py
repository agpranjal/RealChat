from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from django.contrib.auth import authenticate
from privatechat.models import Messages

def home(request):
    count = User.objects.count()
    return render(request, "home.html", {"count":count})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            all_users = list(User.objects.all())
            form.save()
            new_user = authenticate(username=request.POST["username"], password=request.POST["password1"])


            for u in all_users:
                g = Messages(message_from=u.username, message="", user=new_user)
                g.save()
            
                x = Messages(message_from=new_user.username, message="", user=u)
                x.save()

            return redirect("home")
        
    form = UserCreationForm()
    return render(request, "registration/signup.html", {"form":form})

