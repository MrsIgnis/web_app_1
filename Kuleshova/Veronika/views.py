from django.shortcuts import render
from django.http import HttpResponse

def name(request):
    return HttpResponse("Вероника Кулешова")

def groupe(request):
    return HttpResponse("БИН-22-2")

def age(request):
    return HttpResponse("20 лет")

def common(request):
    return HttpResponse("Вероника Кулешова, БИН-22-2, 20 лет")

def index(request):
    return render(request, "home.html")
# Create your views here.
