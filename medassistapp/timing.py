from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from medassistapp.models import Timings

from medassistapp.serializers import TimingsSerializer
from medassistapp.serializers import TimingsGetSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def Submit_Timing(request):
    print("1")
    try:
        if request.method=='POST':
            print("2")
            timing_serializer = TimingsSerializer(data=request.data)
            if timing_serializer.is_valid():
                print(4)
                timing_serializer.save()
                return JsonResponse({"message":'Timing Submitted Successfully',"status":True},safe=False)
            else:
                return JsonResponse({"message":'Fail to submit doctor Timing',"status":False},safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse({"message":'Fail to Submit doctor',"status":False},safe=False)


@api_view(['GET','POST','DELETE'])
def Timings_List(request):
    if request.method=='GET':
        timing_list = Timings.objects.all()
        print("xxx",timing_list)
        doctor_serializer = TimingsGetSerializer(timing_list,many=True)
        return JsonResponse(doctor_serializer.data,safe=False)
    return JsonResponse({},safe=False)


# @api_view(['GET','POST','DELETE'])
# def Doctors_List(request):
#     if request.method=='GET':
#         doctor_list = Doctors.objects.all()
#         print("xxx",doctor_list)
#         doctor_serializer = DoctorSerializer(doctor_list,many=True)
#         return JsonResponse(doctor_serializer.data,safe=False)
#     return JsonResponse({},safe=False)



@api_view(['GET','POST','DELETE'])
def Edit_Timing(request):
    try:
        if request.method=='POST':
            print("XYZ",request.data['id'])
            timings = Timings.objects.get(pk=request.data['id'])
            print(timings)
            timings.doctor_id= request.data['doctor']
            timings.starttimings   = request.data['starttimings']
            timings.endtimings   = request.data['endtimings']
            timings.days   = request.data['days']
            timings.status   = request.data['status']
            print(4)
            timings.save()
            return JsonResponse({"message":'Appointment Edited Successfully',"status":True},safe=False)
        else:
                return JsonResponse({"message":'Appointment unedited',"status":False},safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse({"message":'Fail to Submit Appointment',"status":False},safe=False)


@api_view(['GET','POST','DELETE'])
def Delete_Timing(request):
    try:
        if request.method=='POST':
           
            timings=Timings.objects.get(pk=request.data['id'])
            timings.delete()
            return JsonResponse({'message':'Doctor Session Delete Successfully','status':True},safe=False)
        else:
                return JsonResponse({"message":'Fail to delete doctor',"status":False},safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse({"message":'Fail to Delete doctor record ',"status":False},safe=False)
    

@api_view(['GET','POST','DELETE'])
def Appointment_List(request):
    if request.method=='POST':
        ddoctorid = request.data['doctorid']
        print("rtrtrtrt",ddoctorid)
        timing_list = Timings.objects.all().filter(doctor_id=ddoctorid)
        print("xxx",timing_list)
        doctor_serializer = TimingsGetSerializer(timing_list,many=True)
        return JsonResponse(doctor_serializer.data,safe=False)
    return JsonResponse({},safe=False)


