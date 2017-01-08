# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import menu
from .models import specialmenu
from .forms import specialUserForm
import datetime

def viewmenu(request):
    latest_menu_list = menu.objects.order_by('-id')[:1000]
    template = loader.get_template('menu/index.html')
    context = {
        'latest_menu_list': latest_menu_list,
    	}
    return HttpResponse(template.render(context, request))
    
def detail(request, menu_id):
    question = get_object_or_404(menu, pk=menu_id)
    return render(request, 'menu/detail.html', {'question': question})


def results(request, menu_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % menu_id)

def display(request):
  return render_to_response('index.html', {'obj': models.menu.objects.all()})

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .models import menu as Users
from .forms import UserForm
from django.shortcuts import redirect
from .models import menu


def post(request):
        
        if request.method == "POST":
                form = UserForm(request.POST)
                if form.is_valid():
                    latest_menu_list = menu.objects.order_by('-id')[:1000]
                    post = form.save(commit=False)
                    post.save()
                    context ={'latest_menu_list': latest_menu_list,}
                    return render(request, "menu/index.html",context)
        else:
                form = UserForm()
                
        return render(request, 'menu/update.html', {'form': form})
        
    
        
def post_delete(request, menu_id):
        instance=get_object_or_404(menu, pk=menu_id)
        instance.deleted()
        messages.success(request, "succesfully deleted")
        #return redirect('detail',pk=post.pk)


### SPECIAL MENU CODE SECTION

def specialviewmenu(request):
    latest_menu_list = specialmenu.objects.order_by('-id')[:1000]
    template = loader.get_template('menu/specialindex.html')
    context = {
        'latest_menu_list': latest_menu_list,
        }
    return HttpResponse(template.render(context, request))
    
def specialdetail(request, menu_id):
    question = get_object_or_404(menu, pk=_id)
    return render(request, 'menu/specialdetail.html', {'question': question})


def specialresults(request, menu_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % menu_id)

def specialdisplay(request):
  return render_to_response('specialindex.html', {'obj': models.specialmenu.objects.all()})

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .models import menu as Users
from .forms import UserForm
from django.shortcuts import redirect
from .models import menu


def specialpost(request):
        
        if request.method == "POST":
                form = specialUserForm(request.POST)
                if form.is_valid():
                    latest_menu_list = specialmenu.objects.order_by('-id')[:1000]
                    post = form.save(commit=False)
                    post.save()
                    context ={'latest_menu_list': latest_menu_list,}
                    return render(request, "menu/specialindex.html",context)
        else:
                form = specialUserForm()
                
        return render(request, 'menu/specialupdate.html', {'form': form})
        
    
        
def specialpost_delete(request, menu_id):
        instance=get_object_or_404(menu, pk=menu_id)
        instance.deleted()
        messages.success(request, "succesfully deleted")
        #return redirect('detail',pk=post.pk)

#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % menu_id)

#open dashboard for manager
def managerview(request):
    template = loader.get_template('menu/welcome.html')
    return render(request, "menu/welcome.html", {'time' : datetime.datetime.now()})

## CUSTOMER SURVEYYY##############

from .models import survey
from .forms import customersurvey
def viewsurvey(request):
    latest_menu_list1 = survey.objects.order_by('-id')[:1000]
    template = loader.get_template('menu/survey.html')
    context = {
        'latest_menu_list1': latest_menu_list1,
        }
    return HttpResponse(template.render(context, request))
    
def viewdetail(request, menu_id):
    question = get_object_or_404(menu, pk=menu_id)
    return render(request, 'menu/surveydetail.html', {'question': question})


def viewresults(request, menu_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % menu_id)

def viewdisplay(request):
  return render_to_response('survey.html', {'obj': models.menu.objects.all()})

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .models import menu as Users
from .forms import UserForm
from django.shortcuts import redirect
from .models import menu


def viewpost(request):
        
        if request.method == "POST":
                form = customersurvey(request.POST)
                if form.is_valid():
                    latest_menu_list = survey.objects.order_by('-id')[:1000]
                    post = form.save(commit=False)
                    post.save()
                    context ={'latest_menu_list1': latest_menu_list,}
                    return render(request, "menu/survey.html",context)
        else:
                form = customersurvey()
                
        return render(request, 'menu/surveyupdate.html', {'form': form})
        
    
        
def post_delete(request, menu_id):
        instance=get_object_or_404(menu, pk=menu_id)
        instance.deleted()
        messages.success(request, "succesfully deleted")
        #return redirect('detail',pk=post.pk)



