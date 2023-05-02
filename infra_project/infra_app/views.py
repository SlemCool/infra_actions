from django.http import HttpResponse


def index(request):
    return HttpResponse('Я люблю Git Actions!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
