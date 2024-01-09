"""medassist_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.urls import path
from medassistapp import statecity
from medassistapp import categoryview
from medassistapp import doctor
from medassistapp import timing
from medassistapp import questions
from medassistapp import subquestions
from medassistapp import pateint
from medassistapp import presciption
from medassistapp import answer

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/statelist',statecity.State_List),
    re_path(r'^api/citylist',statecity.City_List),
    re_path(r'^api/categorylist/$',categoryview.Category_List),
    re_path(r'^api/doctorsubmit',doctor.Submit_Doctor),
    re_path(r'^api/doctorlist',doctor.Doctors_List),
    re_path(r'^api/doctoredit',doctor.Edit_Doctor),
    re_path(r'^api/doctordelete',doctor.Delete_Doctor),
    



    ################ TIMING ########################
    re_path(r'^api/timingsubmit',timing.Submit_Timing),
    re_path(r'^api/dtiminglist',timing.Timings_List),
    re_path(r'^api/timingedit',timing.Edit_Timing),
    re_path(r'^api/deletetiming',timing.Delete_Timing),
    # re_path(r'^api/timinglist',timing.Timings_List),
    re_path(r'^api/appointmentlist',timing.Appointment_List),

    ############## Questions ####################
    #  re_path(r'^api/questionlist',questions.QuestionList),
    #  re_path(r'^api/subquessubmit',subquestions.SubQuestion_Submit),
    re_path(r'^api/questionsubmit',questions.QuestionSubmit),
    re_path(r'^api/subquestionsubmit',subquestions.SubQuestionsSubmit),
    re_path(r'^api/questionlist',questions.QuestionList),



     #####################Patient###########
     re_path(r'^api/patientsubmit',pateint.Patient_Submit),
     re_path(r'^api/displaypatient',pateint.Patient_List),
     re_path(r'^api/editpatient',pateint.Edit_Patient),
     re_path(r'^api/deletepatient',pateint.Delete_Patient),
     re_path(r'^api/patientsearch',pateint.Patient_Search),


     #################DoctorLogin###############
     re_path(r'^api/doctorsearch',doctor.Doctor_Search),
     re_path(r'^api/doctorquestions',doctor.Doctor_Questions),


     #######################PrescriptionSubmit#######
     re_path(r'^api/prescriptionsubmit',presciption.Prescription_Submit),
     re_path(r'^api/docprescriptionlist',presciption.Prescription_List),



     ###################### ANswers Submit########
     re_path(r'^api/submitanswer',answer.AnswerSubmit),
     re_path(r'^api/answerlist',answer.Answer_List),
     re_path(r'^api/listdoctor',answer.Doctor_List),
     re_path(r'^api/sendpdf',answer.Edit_Answer),
     re_path(r'^api/transaction',answer.Transaction_History),


]
