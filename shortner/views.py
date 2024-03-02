from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, Http404, HttpResponseNotAllowed
from .models import Url, MAXLENGTH_UUID, Api_Keys
from time import time
import secrets
# import random
# creating collision of uuid
# import uuid
import json
import re


# ------------------------------------------------------- BUISNESS LOGIC ----------------------------------------------------------------------

# characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def __parse_url(link):
    if len(link) > 10000:
        return False

    # true then good link!
    if re.match("(http|https)://", link):
        return link

    # true if the url entered doesnt have http/https but it is correct url!
    if re.match("[A-Za-z0-9+&@#\/%?=~_|!:,;]*[.]+[a-z0-9+&@#\/%=~_|]", link):
        return "https://" + link


def __get_id(link:str) -> str:
        
        # VERY SLOW
        # if URL already Exist! then don't make any other uid!
        # if Url.objects.filter(link=link).exists():
            # return Url.objects.get(link=link).uuid

        # Vulnerable?
        # uid = "".join([random.choice(characters) for _ in range(MAXLENGTH_UUID)])

        uid = secrets.token_urlsafe(MAXLENGTH_UUID-2)

        new_url = Url(link=link, uuid=uid)
        new_url.save()

        return uid

# -------------------------------------------------- ROUTES-VIEWS -------------------------------------------------------------


# Create your views here.
def home(request):
    # we are able to get index.html like this because we a
    return render(request, "index.html")


def create(request):
    if request.method == "POST":
        link = __parse_url(request.POST["link"])
        
        # return empty http response!
        if link == None:
            return HttpResponseBadRequest("BAD KEYWORD")
        else:
            return HttpResponse(__get_id(link))
    else :
        return HttpResponseBadRequest("GET REQUEST, NOT SUPPORTED!")


def go(request, pk):
    try:
        url_details = Url.objects.get(uuid=pk)
        return redirect(url_details.link)
    except Url.DoesNotExist:
        return render(request, "error.html")
        

def api_create(request, key):
    default = json.dumps({"error":"404", "message":"only POST request is accepted"})
    if request.method == "GET":
        if Api_Keys.objects.filter(api_key=key).exists():
            data = request.body
            try:
                data = json.loads(data)
            except Exception:
                return HttpResponseBadRequest("NO BODY FOUND")

            link = data.get("url")
            # url not found in body json
            if link == None:
                return HttpResponseBadRequest("NO URL FOUND IN PAYLOAD")

            link = __parse_url(link)
            # parsing fails for the link
            if link == None:
                return HttpResponseBadRequest("BAD URL FORMAT")
            
            data["shorturl"] = __get_id(link)
            # parse the url
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponseBadRequest("BAD SERVER REQUEST")
    else:
        return HttpResponse(default)