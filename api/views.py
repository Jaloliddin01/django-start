from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

def home(request: HttpRequest):
    args = request.GET

    data = {
        'result' : sum(map(int, args.values())),
    }

    return JsonResponse(data)
