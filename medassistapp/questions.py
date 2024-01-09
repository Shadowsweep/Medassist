from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from medassistapp.models import Category
from medassistapp.models import Questions
from medassistapp.serializers import CategorySerializer
from medassistapp.serializers import QuestionSerializer
from rest_framework.decorators import api_view
@api_view(['Get','POST','DELETE'])
def QuestionList(request):
    try:
        if(request.method=='POST'):
            id=request.data['id']
            questionlist=Questions.objects.all().filter(category_id=id)
            question_serializer=QuestionSerializer(questionlist,many=True)
            return JsonResponse(question_serializer.data,safe=False)
        return JsonResponse({},safe=False)
    except Exception as error:
        print("xxxxxxxxxx",error)
        return JsonResponse({},safe=False)
@api_view(['Get','POST','DELETE'])
def QuestionSubmit(request):
    try:
        if(request.method=="POST"):
            question_serializer=QuestionSerializer(data=request.data)
            if question_serializer.is_valid():
                question_serializer.save()
                return JsonResponse({'message':'Questions submitted sucessfully','status':True},safe=False)
            else:
                return JsonResponse({'message':'Fail to submit questions','status':False},safe=False) 
    except Exception as error:
        print("Error:",error)
        return JsonResponse({'message':'Fail to submit questions','status':False},safe=False)