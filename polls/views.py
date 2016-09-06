from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Noel David S")

def test():
    return HttpResponse("Test")
