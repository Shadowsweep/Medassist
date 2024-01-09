from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from medassistapp.models import Patient
from medassistapp.serializers import PatientSerializer

from rest_framework.decorators import api_view


@api_view(['GET','POST','DELETE'])
def Patient_Submit(request):
    print("1")
    try:
        if request.method=='POST':
            print("2")
            patient_serializer = PatientSerializer(data=request.data)
            print(patient_serializer)
            if(patient_serializer.is_valid()):
                print(9)
                patient_serializer.save()
                return JsonResponse({"message":'Patient Request Submitted Successfully',"status":True},safe=False)
            else:
                return JsonResponse({"message":'Fail to submit request',"status":False},safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse({"message":'Failure in record submit ',"status":False},safe=False)
    

@api_view(['GET','POST','DELETE'])
def Edit_Patient(request):
    try:
        if request.method=='POST':
           
            patient = Patient.objects.get(pk=request.data['id'])
            print(patient)
          
            patient.username   = request.data['patientname']
            patient.city   = request.data['city']
            patient.emailid   = request.data['emailid']
            patient.mobileno   = request.data['mobileno']
            patient.dob   = request.data['dob']
            # patient.gender  = request.data['gender']
            print(4)
            patient.save()
            return JsonResponse({"message":'Patient Record Edited Successfully',"status":True},safe=False)
        else:
                return JsonResponse({"message":'Fail to submit patient',"status":False},safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse({"message":'Fail to Patient Record doctor',"status":False},safe=False)


@api_view(['GET','POST','DELETE'])
def Delete_Patient(request):
    try:
        if request.method=='POST':
           
            patient =Patient.objects.get(pk=request.data['id'])
            print(patient)
            print(4)
            patient.delete()
            return JsonResponse({"message":'Patient Record Deleted Successfully',"status":True},safe=False)
        else:
                return JsonResponse({"message":'Fail to delete patient Record',"status":False},safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse({"message":'Fail to Submit Patient Record',"status":False},safe=False)
    

@api_view(['GET','POST','DELETE'])
def Patient_List(request):
    if request.method=='GET':
        patient_list = Patient.objects.all()
        # print("xxx",doctorlist)
        patient_serializer = PatientSerializer(patient_list,many=True)
        return JsonResponse(patient_serializer.data,safe=False)
    return JsonResponse({},safe=False)

@api_view(['GET','POST','DELETE'])
def Patient_Search(request):
    if request.method=='POST':
        print("111")
        email = request.data['emailid']
        pswd = request.data['password']
        # print("xxx",doctorlist)
        patient = Patient.objects.all().filter(emailid=email,password=pswd)
        patient_serializer = PatientSerializer(patient,many=True)
        print(len(patient_serializer.data))
        if len(patient_serializer.data)==1:
            return JsonResponse({"data":patient_serializer.data,"status":True},safe=False)
        else:
            return JsonResponse({"data":{},"status":False},safe=False)
