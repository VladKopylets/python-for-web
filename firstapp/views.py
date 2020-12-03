from django.shortcuts import render


def index(request):
    return render(request, "firstapp/index.html")


def business(request):
    return render(request, "firstapp/business-v2.html")


def business_ua(request):
    return render(request, "firstapp/businessUA-v2.html")


def creative(request):
    return render(request, "firstapp/creative.html")


def creative_ua(request):
    return render(request, "firstapp/creativeUA-v2.html")
