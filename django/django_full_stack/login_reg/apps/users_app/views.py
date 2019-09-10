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
            request.session['fname'] = result[0].first_name
            messages.add_message(request, messages.INFO, 'Successfully logged in!', extra_tags="success")
            return redirect('/success')
    
    messages.add_message(request, messages.WARNING, 'Login Failed', extra_tags="loginError")
    print('no')
    return redirect('/')

########## SUCCESS RENDER PAGE ##########
def wall(request):
    if 'id' not in request.session:
        messages.add_message(request, messages.ERROR, 'You need to be logged in to access the next page', extra_tags="successError")
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['id']),
            'wall_messages': Message.objects.all(),
        }
        return render(request, 'users_app/wall.html',context)

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
        request.session['fname'] = newUser.first_name
        messages.add_message(request, messages.INFO, 'User successfully created!', extra_tags="success")
        return redirect('/success')

########## POST MESSAGE PROCESS ROUTE ############
def post_message(request):
    user = User.objects.get(id=request.session['id'])
    Message.objects.create(user_id=user, message=request.POST['message'])
    messages.add_message(request, messages.INFO, 'Message posted!', extra_tags="message")
    return redirect('/success')

########### POST COMMENT PROCESS ROUTE #############
def post_comment(request):
    user = User.objects.get(id=request.session['id'])
    message = Message.objects.get(id=request.POST['messageID'])
    Comment.objects.create(message_id = message, user_id=user, comment = request.POST['comment'])
    return redirect('/success')

########## DELETE MESSAGE PROCESS ROUTE ##########
def delete_message(request, id):
    message = Message.objects.get(id=id)
    message.delete()
    return redirect('/success')

########## REMOVE SESSION #############
def logout(request):
    if 'id' in request.session:
        del request.session['id']
    if 'fname' in request.session:
        del request.session['fname']
    return redirect('/')
