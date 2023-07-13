from django.shortcuts import render
from django.http import HttpResponse
from .models import HTMLTag

from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "home.html")


@csrf_exempt
def tag_name(request, tag_name):
    try:
        fragment = HTMLTag.objects.get(html_tag=tag_name.lower())
    except HTMLTag.DoesNotExist:
        return HttpResponse(
            "We don't have a html tag called "
            + tag_name
            + ". Please try again with a common html ."
        )
    if request.method == "GET":
        return HttpResponse(fragment.content)
    elif request.method == "POST":
        values = request.POST.values()
        return HttpResponse(
            fragment.content + "You Posted the following values: " + " ".join(values)
        )
    elif request.method == "PUT":
        values = request.PUT.values()
        return HttpResponse(
            fragment.content + "You Put the following values: " + " ".join(values)
        )
    elif request.method == "DELETE":
        return HttpResponse("Delete Request Received")
