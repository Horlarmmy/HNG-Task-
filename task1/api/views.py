from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def get_data(request):
    data = { "slackUsername": "Horlarmmy", "backend": True, "age": 22, "bio": "My name is Alade Toheeb, I am a Backend Developer || Blockchain Developer. I am always willing to learn and collaborate" }
    return Response(data)

@api_view(['GET', 'POST'])
def calculate(request):
    if (request.method=='POST'):
        data = request.POST
        operation_type = data.get('operation_type')
        print(operation_type)
        return Response(operation_type)

    else:
        return Response("You no go like perform a POST request ???")

