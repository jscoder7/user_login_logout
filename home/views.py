# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib.auth import logout,login

# # Create your views here.
# def index(request):
#     if request.user.is_anonymous:
#         return render(request,'login.html')

#     return render(request,'index.html')
# def loginuser(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         # checking condition here
#         User = authenticate(username=username, password=password)
#         if User is not None:
#             login(User,request)
#             return redirect("/")
#         else:
#             return render(request,'login.html') 
            
            


#     return render(request,'login.html')
# def logoutuser(request):
#     logout(request)
#     return redirect("login.html") 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# password for test user is Harry$$$***000
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")