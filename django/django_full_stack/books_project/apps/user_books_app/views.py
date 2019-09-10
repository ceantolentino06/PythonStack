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
    return render(request, 'user_books_app/index.html', context)

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
            'user': User.objects.get(id=request.session['id']),
            'books': Book.objects.all()
        }
        return render(request, 'user_books_app/books.html',context)

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

############ ADD BOOK ROUTE PROCESS #############
def add_book(request):
    errors = Book.objects.book_validator(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/success')
    else:
        title = request.POST['title']
        desc = request.POST['desc']
        user = User.objects.get(id=request.session['id'])

        newBook = Book.objects.create(title=title, description=desc, uploaded_by=user)
        user.liked_books.add(newBook)
        return redirect('/success')

############ ADD TO FAVS SUCCES ROUTE PROCESS ##########
def add_to_fav_success(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['id'])

    user.liked_books.add(book)
    return redirect('/success')

############ ADD TO FAVS VIEW ROUTE PROCESS ############
def add_to_fav_view(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['id'])

    user.liked_books.add(book)
    return redirect('/books/'+str(book_id))


############ VIEW BOOK ROUTE #################
def show(request, book_id):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'book': Book.objects.get(id=book_id)
    }
    print(context['user'].id)
    print(context['book'].uploaded_by)
    return render(request, 'user_books_app/view.html', context)

############ UPDATE BOOK POST ROUTE ###########
def update(request, book_id):
    errors = Book.objects.book_validator(request.POST)

    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/books/'+str(book_id))
    else:
        book = Book.objects.get(id=book_id)
        book.title = request.POST['title']
        book.description = request.POST['desc']
        book.created_at = datetime.today()
        book.save()
        return redirect('/books/'+str(book_id))

############ DELETE BOOK POST PROCESS ############
def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/success')

########### REMOVE TO FAV PROCESS ROUTE ###########
def remove_to_fav(request, book_id):
    user = User.objects.get(id=request.session['id'])
    book = Book.objects.get(id=book_id)
    user.liked_books.remove(book)
    return redirect('/books/'+str(book_id))

########## LOGOUT REMOVE SESSION #############
def logout(request):
    del request.session['id']
    return redirect('/')
