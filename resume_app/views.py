from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
#from .models import feature


# Create your views here.

def index(request):
    if request.method == 'POST':
        #username = request.POST['username']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        address= request.POST['address']
        comment= request.POST['comment']


        if   phonenumber != '' or address != '' or comment != '':
                user = User.objects.create_user( email=email, phonenumber= phonenumber, address=address, comment=comment)
                user.save()
                messages.info(request, 'You message has been sent..')
                return redirect('index')
        else:
            messages.info(request, 'Please fill in the empty text area!')
            return redirect('index')
    
    else:
        messages.info(request, 'Details not registered')
        return render(request, 'index.html')