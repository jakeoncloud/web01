from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # Construct a dictionary to pass to template engine as its context.
    context_dict = {"boldmessage": "This is BOLD!"}
    # Render the tamplate with request and the template context.
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("Rango says here is the about page. <br /> <a href='/rango/'> Home of Rango </a>")
