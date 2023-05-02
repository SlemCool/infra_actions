from django.http import HttpResponse


def index(request):
    return HttpResponse('Привет. Я скрипт!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
