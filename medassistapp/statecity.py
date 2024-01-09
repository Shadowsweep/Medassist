from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from medassistapp.models import States
from medassistapp.models import City
from medassistapp.serializers import CategorySerializer
from medassistapp.serializers import StateSerializer
from medassistapp.serializers import CitySerializer

from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def State_List(request):
    if request.method=='GET':
        state_list = States.objects.all()
        print("xxx",state_list)
        state_serializer = StateSerializer(state_list,many=True)
        return JsonResponse(state_serializer.data,safe=False)
    return JsonResponse({},safe=False)

# post is used meaning with query and get is used without query

@api_view(['GET','POST','DELETE' ])
def City_List(request):
    if request.method=='POST':
        
        id=request.data['id']
        print('cccc',id)
        citylist = City.objects.all().filter(states_id=id)
        print("xxx",citylist)
        city_serializer = CitySerializer(citylist,many=True)
        print('City data',city_serializer.data)
        return JsonResponse(city_serializer.data,safe=False)
    return JsonResponse({},safe=False)

