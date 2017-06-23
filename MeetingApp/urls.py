"""Сопостовление адресов с функциями"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import login

from MeetingApp.views import registerUser, loginUser, sendMessage, logoutUser, getMessages, test, getData, acceptChange

urlpatterns = [
    url(r'^register/', registerUser),
    url(r'^login/', loginUser),
    url(r'^logout/', logoutUser),
    url(r'^send/', sendMessage),
    url(r'^get/', getMessages),
    url(r'^test/', test),
    url(r'^getData/', getData),
    url(r'^acceptChange/', acceptChange)
]
