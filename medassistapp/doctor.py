from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from medassistapp.models import Doctors
from medassistapp.serializers import DoctorGetSerializer
from medassistapp.serializers import DoctorSerializer
from rest_framework.decorators import api_view
from medassistapp.models import Questions
from medassistapp.serializers import QuestionSerializer
from medassistapp.serializers import QuestionGetSerializer
from medassistapp.models import SubQuestions
from medassistapp.serializers import SubQuestionsGetSerializer
from medassistapp.serializers import SubQuestionsSerializer

@api_view(['GET','POST','DELETE'])
def Submit_Doctor(request):
    print("1")
    try:
        if request.method=='POST':
            print("2")
            doctor_serializer = DoctorSerializer(data=request.data)
            if(doctor_serializer.is_valid()):
                print(4)
                doctor_serializer.save()
                return JsonResponse({"message":'Doctor Submitted Successfully',"status":True},safe=False)
            else:
                return JsonResponse({"message":'Fail to submit doctor',"status":False},safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse({"message":'Fail to Submit doctor',"status":False},safe=False)


@api_view(['GET'])
def Doctors_List(request):
    if request.method=='GET':
        doctorlist = Doctors.objects.all()
        # print("xxx",doctorlist)
        doctor_serializer = DoctorGetSerializer(doctorlist,many=True)
        return JsonResponse(doctor_serializer.data,safe=False)
    return JsonResponse({},safe=False)

# @api_view(['GET','POST','DELETE' ])
# def Mobile_List(request):
#     if request.method=='POST':
        
#         mobilenum=request.data['mobileno']
#         print('cccc',mobilenum)
#         mobilelist = Doctors.objects.all().filter(mobileno=mobilenum)
#         print("xxx",mobilelist)
#         mobile_serializer = DoctorSerializer(mobilelist,many=True)
#         print('mobile data',mobile_serializer.data)
#         return JsonResponse(mobile_serializer.data,safe=False)
#     return JsonResponse({},safe=False)\

@api_view(['GET','POST','DELETE'])
def Edit_Doctor(request):
    try:
        if request.method=='POST':
           
            doctors = Doctors.objects.get(pk=request.data['id'])
            print(doctors)
            doctors.category_id= request.data['category']
            doctors.doctorname   = request.data['doctorname']
            doctors.states_id   = request.data['states']
            doctors.city_id   = request.data['city']
            doctors.address   = request.data['address']
            doctors.qualification   = request.data['qualification']
            doctors.emailid   = request.data['emailid']
            doctors.mobileno   = request.data['mobileno']
            doctors.dob   = request.data['dob']
            doctors.gender  = request.data['gender']
            print(4)
            doctors.save()
            return JsonResponse({"message":'Doctor Edited Successfully',"status":True},safe=False)
        else:
                return JsonResponse({"message":'Fail to submit doctor',"status":False},safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse({"message":'Fail to Submit doctor',"status":False},safe=False)


@api_view(['GET','POST','DELETE'])
def Delete_Doctor(request):
    try:
        if request.method=='POST':
           
            doctors = Doctors.objects.get(pk=request.data['id'])
            print(doctors)
            print(4)
            doctors.delete()
            return JsonResponse({"message":'Doctor Deleted Successfully',"status":True},safe=False)
        else:
                return JsonResponse({"message":'Fail to delete doctor',"status":False},safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse({"message":'Fail to Submit doctor',"status":False},safe=False)
    

@api_view(['GET','POST','DELETE'])
def Edit_Picture(request):
    try:
        if request.method=='POST':
           
            doctors = Doctors.objects.get(pk=request.data['id'])
            doctors.photograph=request.data['photograph']
            print(doctors)
            print(4)
            doctors.save()
            return JsonResponse({"message":'Doctor Img  Edited Successfully',"status":True},safe=False)
        else:
                return JsonResponse({"message":'Fail to delete doctor',"status":False},safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse({"message":'Fail to Submit doctor',"status":False},safe=False)
    

    
@api_view(['GET','POST','DELETE'])
def Doctor_Search(request):
    if request.method=='POST':
        print("111")
        email = request.data['emailid']
        pswd = request.data['password']
        # print("xxx",doctorlist)
        doctor = Doctors.objects.all().filter(emailid=email,password=pswd)
        # doctor = Doctors.objects.all().filter(emailid=email)
        doctor_serializer = DoctorSerializer(doctor,many=True)
        print(len(doctor_serializer.data))
        if len(doctor_serializer.data)==1:
            return JsonResponse({"data":doctor_serializer.data,"status":True},safe=False)
        else:
            return JsonResponse({"data":{},"status":False},safe=False)
        

@api_view(['GET','POST','DELETE'])
def Doctor_Questions(request):
     if request.method=='POST':
        # print("111")
        doctorid = request.data['doctorid']
        print("11111111",doctorid)
        questions = SubQuestions.objects.all().filter(doctor_id = doctorid)
        # print("questions",questions)
        # doctor = Doctors.objects.all().filter(emailid=email)
        questions_serializer = SubQuestionsGetSerializer(questions,many=True)
        return JsonResponse({"data":questions_serializer.data,"status":True},safe=False)
    
     else:
            return JsonResponse({"data":[],"status":False},safe=False)
   
    

