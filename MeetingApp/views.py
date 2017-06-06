import json
from django.http import HttpResponse
from MeetingApp.models import User, Message
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def registerUser(request):
    b = json.load(request)
    newUser = User(email=b['email'], password=b['password'], name=b['name'], surname=b['surname'], city=b['city'])
    all = User.objects.all()
    for x in all:
        if x.email == newUser.email:
            print("User with email " + newUser.email + " already registered!")
            return HttpResponse("error")

    newUser.save()
    print("New user registered:")
    print("Email: " + newUser.email)
    print("Name: " + newUser.name)
    print("Pass: " + newUser.password)
    return HttpResponse("ok")


@csrf_exempt
def loginUser(request):
    b = json.load(request)
    print("Login:")
    print("Email " + b['email'])
    print("Password " + b['password'])
    all = User.objects.all()
    for x in all:
        if x.email == b['email'] and x.password == b['password']:
            response = HttpResponse("ok")
            response.set_cookie("email", b['email'])
            response.set_cookie("password", b['password'])
            print("Success")
            return response
    else:
        print("Error")
        return HttpResponse("Login aborted")


@csrf_exempt
def logoutUser(request):
    response = HttpResponse("ok")
    response.set_cookie("email", "")
    response.set_cookie("password", "")
    return response


@csrf_exempt
def sendMessage(request):
    b = json.load(request)
    message = Message(senderId=b['senderId'], targetId=b['targetId'])
    message.save()
    return HttpResponse("ok")


@csrf_exempt
def getMessages(request):
    user = request.COOKIES["email"]
    all = Message.objects.all()
    response = []
    for x in all:
        if x.targetEmail == user.email:
            response.append(x.message)
    return HttpResponse(response)