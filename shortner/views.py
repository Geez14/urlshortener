from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, Http404, HttpResponseNotAllowed
from .models import Url, MAXLENGTH_UUID, Api_Keys
import time
import uuid
import json
import re


# ------------------------------------------------------- BUISNESS LOGIC ----------------------------------------------------------------------

def __parse_url(link):
    start = time.time()
    if len(link) > 10000:
        print(f"Time to calculate badlink size: {start-time.time()}")
        return False

    # true then good link!
    if re.match("(http|https)://", link):
        print(f"Time to pass level1 parsing: {time.time()-start}")
        return link

    # true if the url entered doesnt have http/https but it is correct url!
    if re.match("[A-Za-z0-9+&@#\/%?=~_|!:,;]*[.]+[a-z0-9+&@#\/%=~_|]", link):
        print(f"Time to pass level-2 parsing: {time.time()-start}")
        return "https://" + link

    # else return false, so we can reject link generation!
    print(f"Time to fail parsing: {time.time()-start}")



def __get_id(link:str) -> str:

        # if URL already Exist! then don't make any other uid!
        if Url.objects.filter(link=link).exists():
            return Url.objects.get(link=link).uuid

        uid = str(uuid.uuid4())[:MAXLENGTH_UUID]
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
            if link == None:
                return HttpResponseBadRequest("NO URL FOUND IN PAYLOAD")

            link = __parse_url(link)

            if link == None:
                return HttpResponseBadRequest("BAD URL FORMAT")
            
            data["shorturl"] = __get_id(link)
            # parse the url
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponseBadRequest("BAD SERVER REQUEST")
    else:
        return HttpResponse(default)