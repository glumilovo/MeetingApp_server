from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource
from MeetingApp.models import User, Message


class UserResource(ModelResource):
    model = User
    fields = ('email', 'password', 'name', 'surname', 'city')


class MessageResource(ModelResource):
    model = Message
    fields = ('senderEmail', 'targetEmail', 'message')

