from django.http import HttpResponse
import random

def hello_world(request):
    return HttpResponse("Hello world!")

