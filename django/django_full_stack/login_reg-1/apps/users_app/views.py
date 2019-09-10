from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime, date

########## ROOT RENDER PAGE ###########
def index(request):
    context = {
        'date': date.today().strftime("%Y-%m-%d")
    }
    return render(request, 'users_app/index.html', context)

########## LOGIN PROCESS ROUTE ########
def login(request):
    result = User.objects.filter(email = request.POST['login_email'])
    if len(result) > 0:
        if bcrypt.checkpw(request.POST['login_password'].encode(), result[0].password.encode()):
            request.session['id'] = result[0].id
            messages.add_message(request, messages.INFO, 'Successfully logged in!')
            return redirect('/success')
    
    messages.add_message(request, messages.WARNING, 'Login Failed', extra_tags="loginError")
    print('no')
    return redirect('/')

########## SUCCESS RENDER PAGE ##########
def success(request):
    if 'id' not in request.session:
        messages.add_message(request, messages.ERROR, 'You need to be logged in to access the next page', extra_tags="successError")
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['id'])
        }
        return render(request, 'users_app/success.html',context)

########## REGISTER PROCESS ROUTE ###########
def register(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        birthday = request.POST['bday']
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        print(birthday)

        newUser = User.objects.create(first_name=fname, last_name=lname, birthday=birthday, email=email, password=hashed)

        request.session['id'] = newUser.id
        messages.add_message(request, messages.INFO, 'User successfully created!')
        return redirect('/success')

########## REMOVE SESSION #############
def logout(request):
    del request.session['id']
    return redirect('/')
