from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from medassistapp.models import Category
from medassistapp.models import States
from medassistapp.models import City
from medassistapp.serializers import CategorySerializer


from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def Category_List(request):
    if request.method=='GET':
        category_list = Category.objects.all()
        print("xxx",category_list)
        category_serializer = CategorySerializer(category_list,many=True)
        return JsonResponse(category_serializer.data,safe=False)
    return JsonResponse({},safe=False)
