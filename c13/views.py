#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import json
from users import forms


def IndexViews(request):
    return render(request,'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            request.session.set_expiry(60 * 30)
            return HttpResponseRedirect(request.GET.get("next") if request.GET.get("next") else "/")
        else:
            return render(request,'login.html',{'login_err': 'Wrong username or password!'})
    else:
        return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


@login_required
def personal(request):
    if request.method == 'POST':
        msg = {}
        old_passwd = request.POST.get('old_passwd')

        new_password = request.POST.get('new_passwd')
        user = auth.authenticate(username=request.user.email,password=old_passwd)
        if user is not None:
            request.user.set_password(new_password)
            request.user.save()
            msg['msg'] = 'Password has been changed!'
            msg['res'] = 'success'
        else:
            msg['msg'] = 'Old password is incorrect!'
            msg['res'] = 'failed'

        return HttpResponse(json.dumps(msg))
    else:
        return render(request,'personal.html',{'info_form':forms.UserProfileForm()})

