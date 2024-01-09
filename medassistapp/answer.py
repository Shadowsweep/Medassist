from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from medassistapp.models import Answers
from medassistapp.serializers import AnswerSerializer
from medassistapp.serializers import AnswerGetSerializer
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import api_view
 
@api_view(['Get','POST','DELETE'])
def AnswerSubmit(request):
    try:
        if(request.method=="POST"):
            print("data coming")
            answer_serializer=AnswerSerializer(data=request.data)
            # print("answers coming",answer_serializer)
            if answer_serializer.is_valid():
                # print("answers coming",answer_serializer.data)
                print('DATTTTTTAAAAAAAAAAAAAAAAAAAAaa')
                answer_serializer.save()
                # print("answers coming",answer_serializer.data)
                return JsonResponse({'message':'Answer submitted sucessfully','status':True},safe=False)
            else:
                return JsonResponse({'message':'Failllll to submit Answer','status':False},safe=False) 
    except Exception as error:
        print("Error:",error)
        return JsonResponse({'message':'Fail to submi Answer','status':False},safe=False)
    

@api_view(['GET', 'POST', 'DELETE'])
def Answer_List(request):
 if request.method=='POST':
    doctorid=request.data['doctorid']
    print("DOCCC",doctorid)
    answerslist=Answers.objects.all().filter(doctor_id=doctorid)
    answers_serializer = AnswerGetSerializer(answerslist,many=True)
    print("LIST",answers_serializer.data)
    return JsonResponse(answers_serializer.data,safe=False)
 return JsonResponse({},safe=False) 


@api_view(['GET', 'POST', 'DELETE'])
def Doctor_List(request):
 if request.method=='POST':
    patientid=request.data['patientid']
    print("pattttt",patientid)
    answerslist=Answers.objects.all().filter(patient_id=patientid)
    answers_serializer = AnswerGetSerializer(answerslist,many=True)
    print("LIST",answers_serializer.data)
    return JsonResponse(answers_serializer.data,safe=False)
 return JsonResponse({},safe=False) 


@api_view(['GET','POST','DELETE'])
def Edit_Answer(request):
    try:
        if request.method=='POST':
            print("AAiye")
            answers = Answers.objects.get(pk=request.data['answer'])
            answers.emailid   = request.data['emailid']
            print(answers.emailid)
            print(answers)
            answers.prescriptionpdf  = request.data['prescriptionpdf']
            print(4)
            answers.save()
            subject = 'MedAssist Prescription uploaded'       
            recipient_list = [answers.emailid,"techunsatisfied@gmail.com"]
            print(recipient_list)
            send_result = send_mail(subject,'Dear Customer Your Prescription has been Uploaded Please Check ', settings.EMAIL_HOST_USER, recipient_list)
            # print("Done")
            if send_result:
                message = 'Prescription PDF Sent'
                print("Bawandar")
                status = True
            else:
                    # Email sending failed
                message = 'Failed to send Prescription PDF'
                status = False

                   # Return the result to be used for displaying the message
            return JsonResponse({"message": message, "status": status}, safe=False)
            
                 
        else:
                return JsonResponse({"message":'Fail to submit Prescription',"status":False},safe=False)
    except Exception as e:
        print("Error",e)
        return JsonResponse({"message":'Fail to Submit Prescription',"status":False},safe=False)
    
    
@api_view(['GET', 'POST', 'DELETE'])
def Transaction_History(request):
 if request.method=='POST':
    
    answerslist=Answers.objects.all()
    answers_serializer = AnswerGetSerializer(answerslist,many=True)
    print("LIST",answers_serializer.data)
    return JsonResponse(answers_serializer.data,safe=False)
 return JsonResponse({},safe=False) 