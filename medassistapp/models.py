from django.db import models

# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=70, blank=False, default='')
    description= models.CharField(max_length=200,blank=False, default='')
    icon = models.CharField(max_length=250,blank=False, default='')


class States(models.Model):
    statename = models.CharField(max_length=100,blank=False,default='')

class City(models.Model):
    # stateid =  models.BigIntegerField(blank=False)
    states = models.ForeignKey(States,on_delete=models.CASCADE)
    cityname = models.CharField(max_length=100,blank=False,default='')

class Doctors(models.Model):


    # categoryid=models.BigIntegerField(blank=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    doctorname = models.CharField(max_length=100,blank=False,default='')
    gender = models.CharField(max_length=100,blank=False,default='')
    dob= models.CharField(max_length=100,blank=False,default='')
    address = models.CharField(max_length=100,blank=False,default='')
    states = models.ForeignKey(States,on_delete=models.CASCADE)
   # stateid =  models.BigIntegerField(blank=False)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    emailid = models.CharField(max_length=100,blank=False,default='')
    mobileno = models.CharField(max_length=100,blank=False,default='')
    qualification = models.CharField(max_length=100,blank=False,default='')
    photograph = models.ImageField(upload_to='static/')
    password = models.CharField(max_length=100, blank=False, default='')

class Timings(models.Model):
    # doctorid=models.BigIntegerField(blank=False)
    doctor = models.ForeignKey(Category,on_delete=models.CASCADE)
    starttimings = models.CharField(max_length=100,blank=False,default='')
    endtimings = models.CharField(max_length=100,blank=False,default='')
    days= models.CharField(max_length=100,blank=False,default='')
    status = models.CharField(max_length=100,blank=False,default='')
     
class Questions(models.Model):
    doctor=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    questionnumber=models.CharField(max_length=200,blank=False,default='')
    question=models.CharField(max_length=200,blank=False,default='')
class SubQuestions(models.Model):
    doctor=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    subquestionnumber=models.CharField(max_length=200,blank=False,default='')
    subquestiontext=models.CharField(max_length=200,blank=False,default='')
    subquestion=models.CharField(max_length=200,blank=False,default='')
    
class Patient(models.Model):
    username=models.CharField(max_length=200,blank=False,default='')
    city=models.CharField(max_length=200,blank=False,default='')
    emailid=models.CharField(max_length=200,primary_key=True)
    dob=models.CharField(max_length=200,blank=False,default='')
    mobileno=models.CharField(max_length=200,blank=False,default='')
    password=models.CharField(max_length=200,blank=False,default='') 
    gender=models.CharField(max_length=200,blank=False,default='')



    
class Answers(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    currentdate=models.CharField(max_length=200,blank=False,default='')
    currenttime=models.CharField(max_length=200,blank=False,default='') 
    ansdata=models.CharField(max_length=4000,blank=False,default='')
    # prespdf=models.CharField(max_length=4000,blank=False,default='')
    prescriptionpdf = models.ImageField(upload_to='static/', default=None, verbose_name='Prescription PDF', blank=True)
    razorpayid=models.CharField(max_length=4000,blank=False,default='')
    

class Prescription(models.Model):
    
    answer=models.ForeignKey(Answers,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    currentdate=models.CharField(max_length=200,blank=False,default='')
    currenttime=models.CharField(max_length=200,blank=False,default='')
    tests=models.CharField(max_length=200,blank=False,default='')
    diet=models.CharField(max_length=200,blank=False,default='')
    medicine=models.CharField(max_length=400,blank=False,default='')