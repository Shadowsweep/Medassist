from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from medassistapp.models import Category
from medassistapp.models import SubQuestions
from medassistapp.serializers import CategorySerializer
from medassistapp.serializers import QuestionSerializer
from medassistapp.serializers import SubQuestionsSerializer
from rest_framework.decorators import api_view

@api_view(['Get','POST','DELETE'])
def SubQuestionList(request):
    try:
        if(request.method=='POST'):
            print("1")
            id=request.data['id']
            print("2")
            subquestionlist=SubQuestions.objects.all()
            print("3")
            subquestion_serializer=SubQuestionsSerializer(subquestionlist,many=True)
            return JsonResponse(subquestion_serializer.data,safe=False)
        return JsonResponse({},safe=False)
    except Exception as error:
        print("xxxxxxxxxx",error)
        return JsonResponse({},safe=False)
    

@api_view(['GET','POST','DELTE'])
def SubQuestionsSubmit(request):
    try:
        if request.method=="POST":
            subquestions_serializer=SubQuestionsSerializer(data=request.data)
            if subquestions_serializer.is_valid():
                subquestions_serializer.save()
                return JsonResponse({'message':'Subquestions Submitted Successfully','status':True},safe=False)
            else:
                return JsonResponse({'message':'Fail to Submit Subquestions','status':False},safe=False)
    except Exception as error:
        print('Error',error)
        return JsonResponse({'messgae':'Fail to submit Subquestions','status':False},safe=False)