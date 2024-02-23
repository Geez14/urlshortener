from django.shortcuts import render, redirect
import uuid
from .models import Url, MAXLENGTH_UUID
from django.http import HttpResponse
import re


# Create your views here.
def home(request):
    # we are able to get index.html like this because we a
    return render(request, "index.html")


def create(request):
    if request.method == "POST":
        link = parse_url(request.POST["link"])

        if link == False:
            # return empty http response!
            return HttpResponse()

        # if URL already Exist! then don't make any other uid!
        if Url.objects.filter(link=link).exists():
            return HttpResponse(Url.objects.get(link=link).uuid)

        uid = str(uuid.uuid4())[:MAXLENGTH_UUID]

        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)


def parse_url(link):
    # true then good link!
    if re.match("(http|https)://", link):
        return link

    # true if the url entered doesnt have http/https but it is correct url!
    if re.match("[A-Za-z0-9+&@#\/%?=~_|!:,;]*[.]+[a-z0-9+&@#\/%=~_|]", link):
        return "https://" + link

    # else return false, so we can reject link generation!
    return False


"""
Check weather the link is available in the table or not!"""
