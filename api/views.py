from django.shortcuts import render
import json
from django.http import HttpRequest, HttpResponse, JsonResponse

def home(request: HttpRequest):
    args = request.GET

    data = {
        'result' : sum(map(int, args.values())),
    }

    return JsonResponse(data)

def get_sum(request: HttpRequest):

    if request.method == "GET":
        return HttpResponse("Ok")

    if request.method == "POST":
        data = json.loads(request.body.decode())
        print(data)
        result = {
            "result": sum(map(int, data.values()))
        }        
        return JsonResponse(result)
