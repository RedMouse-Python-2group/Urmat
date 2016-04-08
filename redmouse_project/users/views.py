# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserForm

def login(request):
    context = {}
    context.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            context['login_error'] = "Пользователь не найден"
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def registration(request):
    context = {}
    context.update(csrf(request))
    context['form'] = UserForm()
    if request.POST:
        newuser_form = UserForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save() # if success go to sign in
            newuser = auth.authenticate(username = newuser_form.cleaned_data['username'],
                                        password = newuser_form.cleaned_data['password'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            context['form'] = newuser_form
    return render(request, 'registration.html', context)
