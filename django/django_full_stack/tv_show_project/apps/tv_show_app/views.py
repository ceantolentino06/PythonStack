from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib import messages
from datetime import datetime, date
def root(request):

    return redirect('/shows')
################# INDEX ROUTE ###################
def index(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'tv_show_app/index.html', context)

################# CREATE SHOW PAGE ROUTE ############W
def add_show_render(request):
    context = {
        'date': date.today().strftime("%Y-%m-%d")
    }
    print(context['date'])
    return render(request, 'tv_show_app/create.html',context)

################# CREATE SHOW PROCESS ROUTE ################
def add_show(request):
    errors = Show.objects.basic_validations(request.POST)

    if len(errors) > 0:
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/shows/new')
    else:
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['rel_date']
        desc = request.POST['desc']

        messages.add_message(request, messages.SUCCESS, 'Show successfully added')
        newShow = Show.objects.create(title=title, network=network, release_date=release_date, description=desc)
        print(newShow.id)
        return redirect('/shows/'+str(newShow.id))

################## SHOW SHOW INFORMATION ROUTE #################
def show(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'tv_show_app/view.html', context)

################# SHOW EDIT ROUTE ##########################
def edit_show_render(request, id):
    show = Show.objects.get(id=id)
    context = {
        'show': show,
        'date': show.release_date.strftime("%Y-%m-%d")
    }
    print(context['date'])
    return render(request, 'tv_show_app/edit.html', context)

################ EDIT PROCESS ROUTE ########################
def edit_show(request):
    errors = Show.objects.basic_validations(request.POST)

    if len(errors) > 0:
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/shows/'+request.POST['showID']+'/edit')
    else:
        show = Show.objects.get(id=request.POST['showID']) 
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['rel_date']
        show.description = request.POST['desc']

        show.save()
        messages.add_message(request, messages.SUCCESS, 'Show successfully updated')
        return redirect('/shows/'+str(show.id))

############### DELETE PROCESS ROUTE ########################
def delete_show(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')



