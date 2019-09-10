from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books_authors_app/index.html', context)

################ ADD BOOK ROUTE ###################
def add_book(request):
    title = request.POST['title']
    desc = request.POST['desc']
    Book.objects.create(title=title, desc=desc)

    return redirect('/')

################ VIEW BOOK ROUTE ####################
def view(request,id):
    context = {
        'book': Book.objects.get(id=id),
        'authors': Author.objects.filter(books = Book.objects.get(id=id)),
        'all_authors': Author.objects.exclude(books = Book.objects.get(id=id))
    }
    return render(request, 'books_authors_app/view.html', context)

################## ADD BOOK AUTHOR ROUTE ###################
def add_book_author(request):
    context = {
        'author_id': request.POST['author'],
        'book_id': request.POST['bookID']
    }
    auth = Author.objects.get(id=request.POST['author'])
    auth.books.add(Book.objects.get(id=request.POST['bookID']))
    return redirect('/books/'+context['book_id'])

################## AUTHOR INDEX #######################
def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'books_authors_app/authors.html', context)

################# ADD AUTHOR #######################
def add_author(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    notes = request.POST['notes']
    Author.objects.create(first_name=fname, last_name=lname, notes=notes)

    return redirect('/authors')

################## VIEW AUTHOR ROUTE ###############
def view_author(request, id):
    context = {
        'author': Author.objects.get(id=id),
        'books': Book.objects.filter(author = Author.objects.get(id=id)),
        'all_books': Book.objects.exclude(author = Author.objects.get(id=id))
    }
    return render(request, 'books_authors_app/view_authors.html', context)

################## ADD BOOKS FOR AUTHOR #################
def add_author_book(request):
    context = {
        'author_id': request.POST['authorID'],
        'book_id': request.POST['book']
    }
    auth = Author.objects.get(id=request.POST['authorID'])
    auth.books.add(Book.objects.get(id=request.POST['book']))
    return redirect('/authors/'+context['author_id'])