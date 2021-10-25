from django.shortcuts import render

# Create your views here.
from django.db.models.signals import post_save
from django.http import JsonResponse, HttpResponse
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from mysite import settings
from .models import User
import os
import re


# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def authentication(request):
    token_str = request.META.get("HTTP_AUTHORIZATION")
    # print(request.META['HTTP_AUTHORIZATION'])
    try:
        token = Token.objects.get(key=token_str)
    except:
        return None
    user = User.objects.get(id=token.user_id)
    return user


def index(request):
    return HttpResponse("Hello, world. You're at the login/register index.")


# Create your views here.
def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    try:
        print('username:', username)
        print('password:', password)
        user = User.objects.get(username=username, password=password)
        token = Token.objects.get(user_id=user.id)
        data = {'token': str(token), 'message': "true"}
    except:
        data = {'token': None, 'message': "false"}
    return JsonResponse(data)


def register(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if not User.objects.filter(username=username):
        print('username:', username)
        print('password: ', password)
        user = User.objects.create(username=username, password=password)
        token = Token.objects.get(user=user)
        data = {'token': str(token), 'user': username, 'message': "true"}
    else:
        data = {'token': None, 'user': username, 'message': "false"}

    return JsonResponse(data)


# 拉取用户信息
def user_info(request):
    print('pull user info')
    user = authentication(request)
    if user is None:
        return HttpResponse('Unauthorized', status=401)
    data = {'username': user.username,
            'password': user.password}
    return JsonResponse(data)
