from django.shortcuts import render, redirect
from django.contrib import messages
from tv_shows_app.models import *

def index(request):
    return redirect('/shows')

def shows_new(request):
    return render(request, "shows_new.html")

def shows_create(request):
    errors = TVshow.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        new_show = TVshow.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
        return redirect('/shows/'+str(new_show.id))

def show_info(request, id):
    context = {
        "show_info" : TVshow.objects.get(id=id)
    }
    return render(request, "shows_info.html", context)

def shows(request):
    context = {
        "all_shows": TVshow.objects.all()
    }
    return render(request, "shows.html", context)

def shows_edit(request, id):
    context = {
        "show_info": TVshow.objects.get(id=id)
    }
    return render(request, "shows_edit.html", context)

def shows_update(request, id):
    errors = TVshow.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/"+str(id)+"/edit")
    else:
        the_book = TVshow.objects.get(id=id)
        the_book.title = request.POST['title']
        the_book.network = request.POST['network']
        the_book.release_date = request.POST['release_date']
        the_book.desc = request.POST['desc']
        the_book.save()
        return redirect("/shows/"+str(the_book.id))

def shows_delete(request, id):
    the_book = TVshow.objects.get(id=id)
    the_book.delete()
    return redirect('/shows')