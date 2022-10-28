from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def get_data(request):
    data = { "slackUsername": "Horlarmmy", "backend": True, "age": 22, "bio": "My name is Alade Toheeb, I am a Backend Developer || Blockchain Developer. I am always willing to learn and collaborate" }
    return Response(data)

