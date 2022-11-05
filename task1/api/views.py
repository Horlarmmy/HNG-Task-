from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

# Create your views here.

@api_view(['GET'])
def get_data(request):
    data = { "slackUsername": "Horlarmmy", "backend": True, "age": 22, "bio": "My name is Alade Toheeb, I am a Backend Developer || Blockchain Developer. I am always willing to learn and collaborate" }
    return Response(data)

@api_view(['GET', 'POST'])
def calculate(request):
    if (request.method=='POST'):
        data = json.loads(request.body.decode())
        operation_type = data.get('operation_type')
        x = int(data.get('x'))
        y = int(data.get('y'))

        if operation_type == "addition":
            res = x + y
        if operation_type == "subtraction":
            res = x - y
        if operation_type == "multiplication":
            res = x * y
        

        data = {"slackUsername": "Horlarmmy", "result": res, "operation_type": operation_type}
        return Response(data)

    else:
        return Response("You no go like perform a POST request ???")

