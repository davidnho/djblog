
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Noel S David")

def test():
    return HttpResponse("Testing lang")

