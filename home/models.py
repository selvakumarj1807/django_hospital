from django.db import models

import datetime
import os

def getFileName(requset,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads',new_filename)

# Create your models here.
class Doctor(models.Model):
    doctor_name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    department=models.CharField(max_length=150,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)   
    
    class Meta:
        db_table = "doctor_details"
        
    def __str__(self) :
        return self.doctor_name


class Appoitment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    select_doctor = models.CharField(max_length=100)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)   


    class Meta:
        db_table = "appoitment"
        
    def __str__(self) :
        return self.name
