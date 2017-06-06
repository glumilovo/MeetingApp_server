from django.conf.urls import url
from django.contrib import admin

from MeetingApp.views import registerUser, loginUser, sendMessage, logoutUser, getMessages

urlpatterns = [
    url(r'^register/', registerUser),
    url(r'^login/', loginUser),
    url(r'^logout/', logoutUser),
    url(r'^send/', sendMessage),
    url(r'^get/', getMessages)
]
