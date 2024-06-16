from django.http import HttpResponse
from django.shortcuts import render


def mouse_entered(request):
    # pylint: disable=unused-argument
    return HttpResponse("Mouse Entered")


def home(request):
    return render(request, "home.html", {})
