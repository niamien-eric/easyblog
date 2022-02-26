from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login,logout,authenticate
User = get_user_model()

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'session/signin.html')

def sign_up(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("confirm_password")
        if password == password_confirm:
            user = User.objects.create_user(username=username,password=password)
            login(request, user)
            return redirect('home')
        else:
            message = 'mot de passe incorrects'
    context = {'message':message}
    return render(request, 'session/signup.html',context)

def sign_out(request):
    logout(request)
    return redirect('home')
