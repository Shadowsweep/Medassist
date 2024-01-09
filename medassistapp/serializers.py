from rest_framework import serializers 
from medassistapp .models import  Category
from medassistapp.models import States
from medassistapp.models import Doctors
from medassistapp.models import City
from medassistapp.models import Timings
from medassistapp.models import Questions
from medassistapp.models import SubQuestions
from medassistapp.models import Patient
from medassistapp.models import Prescription
from medassistapp.models import Answers
class CategorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Category
        fields = '__all__'



class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=States
        fields='__all__'
        
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctors
        fields = '__all__'


class DoctorGetSerializer(serializers.ModelSerializer):
    states = StateSerializer(many=False)
    city=CitySerializer(many=False)
    category=CategorySerializer(many=False)
    class Meta:
        model = Doctors
        fields = '__all__'

class TimingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timings
        fields = '__all__'

class TimingsGetSerializer(serializers.ModelSerializer):
    class Meta:
        doctor=DoctorSerializer(many=False)
        model = Timings
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Questions
        fields="__all__"
class QuestionGetSerializer(serializers.ModelSerializer):
    category=CategorySerializer(many=False)
    doctor=DoctorSerializer(many=False)
    class Meta:
        model=Questions
        fields="__all__"
class SubQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubQuestions
        fields="__all__"
class SubQuestionsGetSerializer(serializers.ModelSerializer):
    category=CategorySerializer(many=False)
    question=QuestionSerializer(many=False)
    doctor=DoctorSerializer(many=False)
    class Meta:
        model=SubQuestions
        fields="__all__"
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields="__all__"    
        

       

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answers
        fields="__all__"
class AnswerGetSerializer(serializers.ModelSerializer):
    patient=PatientSerializer(many=False)
    doctor=DoctorSerializer(many=False)
    class Meta:
        model=Answers
        fields="__all__"   

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prescription
        fields="__all__"         
class PrescriptionGetSerializer(serializers.ModelSerializer):
    patient=PatientSerializer(many=False)
    doctor=DoctorSerializer(many=False)
    class Meta:
        model=Prescription
        fields="__all__"   