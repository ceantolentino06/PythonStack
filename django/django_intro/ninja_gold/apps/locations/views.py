from django.shortcuts import render, HttpResponse,redirect
import time
import random
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, "locations/index.html")

def process_money(request, location):
    if 'activities' not in request.session:
        request.session['activities'] = []
    currTime = time.strftime("%Y-%m-%d %I:%M %p")

    if location == 'farm':
        rand = random.randint(10,20)
        request.session['gold'] += rand
        request.session['activities'].append("Earned {} golds from the {}! ({})".format(rand, location, currTime))
    elif location == 'cave':
        rand = random.randint(5,10)
        request.session['gold'] += rand
        request.session['activities'].append("Earned {} golds from the {}! ({})".format(rand, location, currTime))
    elif location == 'house':
        rand = random.randint(2,5)
        request.session['gold'] += rand
        request.session['activities'].append("Earned {} golds from the {}! ({})".format(rand, location, currTime))
    elif location == 'casino':
        rand = random.randint(-50,50)
        request.session['gold'] += rand
        if rand > 0:
            request.session['activities'].append("Entered a {} and earned {} golds! {}".format(location, rand, currTime))
        else:
            request.session['activities'].append("Entered a {} and lost {} golds... Ouch.. {}".format(location, rand*-1, currTime))
    print(request.session['activities'])
    print(request.session['gold'])
    return redirect('/')

def reset(request):
    del request.session['gold']
    del request.session['activities']
    return redirect('/')