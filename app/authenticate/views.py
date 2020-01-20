from django.shortcuts import render



# Create your views here.
def userAuth(request):
    return render(request, 'user_login_register.html', {})



def adminAuth(request):
    return render(request, 'admin_login_register.html', {})