from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout





# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        return render(request, 'inicio/home.html')
    else:
        return redirect('inicio:login')




def LoginView(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('inicio:index')
        else:
           
            return redirect('inicio:errorlogin')

    return render(request, 'inicio/login.html')




def ErrorLogin(request):
    return render(request, 'inicio/error_login.html')



def LogoutView(request):
    logout(request)
    return redirect('inicio:login')


