from django.shortcuts import render, redirect
from accountsapp.models import User
from django.contrib import auth

def accountsapp(request):
    return render(request, 'accountsapp.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(email=request.POST['email'])
                return render(request, 'accounts/signup.html', {'error': '이미 사용중인 아이디입니다.'})
            except User.DoesNotExist:
                #self.model(email=email, username=username,registered=adress, phone=phone_number, **extra_fields)
                user = User.objects.create_user(
                    email=request.POST['email'], 
                    username=request.POST['username'], 
                    password=request.POST['password1'],
                    registered=request.POST['adress'],
                    phone=request.POST['phone_number']
                    )
                auth.login(request, user)
                return redirect('accountsapp')
        else:
            return render(request, 'signup.html', {'error': '패스워드가 동일해야 합니다.'})
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('accountsapp')
        else:
            return render(request, 'login.html', {'error': 'email or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('accountsapp')
    return render(request, 'signup.html')

