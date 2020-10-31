from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def business(request):
    return render(request, "business-v2.html")


def business_ua(request):
    return render(request, "businessUA-v2.html")


def creative(request):
    return render(request, "creative-v2.html")


def creative_ua(request):
    return render(request, "creativeUA-v2.html")
