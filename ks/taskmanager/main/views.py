from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def blok(request):
    return render(request, 'main/blok1.html')