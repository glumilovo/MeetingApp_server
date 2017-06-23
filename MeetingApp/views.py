import json
from django.http import HttpResponse
from django.http import JsonResponse
from MeetingApp.models import User, Message
from django.views.decorators.csrf import csrf_exempt


""""Регистрация"""
@csrf_exempt
def registerUser(request):
    b = json.load(request)
    newUser = User(email=b['email'], password=b['password'])
    all = User.objects.all()
    for x in all:
        if x.email == newUser.email:
            print("User with email " + newUser.email + " already registered!")
            return HttpResponse("already exists")

    newUser.save()
    print("New user registered:")
    print("Email: " + newUser.email)
    print("Pass: " + newUser.password)
    return HttpResponse("ok")

"Функция логина"
@csrf_exempt
def loginUser(request):
    b = json.load(request)
    print("Login:")
    print("Email " + b['email'])
    print("Password " + b['password'])
    all = User.objects.all()
    for x in all:
        if x.email == b['email'] and x.password == b['password']:
            response = HttpResponse("Success")
            response.set_cookie("email", b['email'])
            response.set_cookie("password", b['password'])
            print("Success")
            return response
    else:
        print("Error")
        return HttpResponse("Login aborted")


"""Выход из профиля"""
@csrf_exempt
def logoutUser(request):
    response = HttpResponse("ok")
    response.set_cookie("email", "")
    response.set_cookie("password", "")
    return response

"""Для чата"""
@csrf_exempt
def sendMessage(request):
    b = json.load(request)
    message = Message(senderId=b['senderId'], targetId=b['targetId'])
    message.save()
    return HttpResponse("ok")

"""Тестовая функция для Logout"""
@csrf_exempt
def test(request):
    response = HttpResponse(request.COOKIES["email"])
    return response

"""Функция для чата"""
@csrf_exempt
def getMessages(request):
    user = request.COOKIES["email"]
    all = Message.objects.all()
    response = []
    for x in all:
        if x.targetEmail == user.email:
            response.append(x.message)
    return HttpResponse(response)


"""Функция редактирования профиля"""
@csrf_exempt
def getData(request):
    if "email" not in request.COOKIES or request.COOKIES["email"] == "":
        return JsonResponse({'status':'error'})

    users = User.objects.all()
    for user in users:
        if user.email == request.COOKIES["email"]:
            return JsonResponse({'status':'ok', 'name':user.name, 'surname':user.surname, 'city':user.city, 'sex':user.sex, 'date_of_birth':user.date_of_birth})

    return JsonResponse({'status':'error'})

"""Функция изменения настроек"""
@csrf_exempt
def acceptChange(request):
    if "email" not in request.COOKIES or request.COOKIES["email"] == "":
        return HttpResponse('error')

    users = User.objects.all()
    for user in users:
        if user.email == request.COOKIES["email"]:
            b = json.load(request)
            user.name = b["name"]
            user.surname = b["surname"]
            user.city = b["city"]
            user.sex = b["sex"]
            user.date_of_birth = b["date_of_birth"]
            user.save()

            return HttpResponse('ok')

    return HttpResponse('error')