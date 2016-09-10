from django.http import HttpResponse

def index(requeset):
    return HttpResponse('Rango says hey there partner!')
