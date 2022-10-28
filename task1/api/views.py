from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def get_data(request):
    data = { "slackUsername": "Horlarmmy", "backend": True, "age": 22, "bio": "Baby" }
    return Response(data)

