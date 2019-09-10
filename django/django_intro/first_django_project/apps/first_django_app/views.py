from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    return render(request, 'first_django_app/index.html')

def random(request):
    request.session['random'] = get_random_string(length=14)
    return redirect('/')