from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length = 150,blank = True,null = True)
    image = models.ImageField(upload_to = '%y/%m/%d/',null = True, blank = True)
    mailaddress = models.EmailField(max_length = 200,blank = True,null= True)
    address = models.CharField(max_length = 300,blank = True,null=True)
    number_validate = RegexValidator(regex = r'^(\+91)[ -]?(\d{3})[ -]?(\d{3})[ -]?(\d{4})',message = "Please enter a valid phone number")
    phone_number = models.CharField(validators=[number_validate],max_length = 16,blank = True,null = True)
    designation = models.CharField(max_length=100,null = True, blank= True)
    orgnization = models.CharField(max_length=150,null = True,blank = True)
    joindate = models.DateField(auto_now_add= False,auto_now = False, null = True,blank= True)
    about_me = models.CharField(max_length=500 , null = True, blank= True)
    about_image = models.ImageField(upload_to ='aboutimage/%y',null=True,blank = True)
    def __str__(self) -> str:
        return self.full_name

class WorkExperience(models.Model):
    person = models.ForeignKey(User,on_delete = models.CASCADE,null = True,blank = True)
    designation = models.CharField(max_length = 100,null = True,blank = True)
    organization = models.CharField(max_length = 300,null = True,blank  = True)
    enddate = models.DateField(auto_now_add = False,auto_now = False,blank = True, null= True)
    joining = models.DateField(auto_now_add = False,auto_now = False,blank = True, null= True)
    detail = models.CharField(null = True,blank = True, max_length = 300)
    def __str__(self) -> str:
        return self.designation    

class Project(models.Model):
    person = models.ForeignKey(User,on_delete = models.CASCADE,null = True,blank = True)
    image = models.ImageField(upload_to='projects/',null = True ,blank = True)
    title = models.CharField(max_length = 100,null = True,blank = True)
    description = models.CharField(max_length = 300,null = True,blank = True)
    def __str__(self) -> str:
        return self.title


class Skill(models.Model):
    person = models.ForeignKey(User,on_delete = models.CASCADE,null = True,blank = True)
    technology = models.CharField(max_length = 100,null = True, blank = True)
    skillpoints = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')
    )
    skillpoint = models.IntegerField(choices = skillpoints,null = True, blank = True)
    def __str__(self) -> str:
        return self.technology


class Intrest(models.Model):
    person = models.ForeignKey(User,on_delete = models.CASCADE,null = True,blank = True)
    area = models.CharField(max_length = 150, null = True, blank = True)
    def __str__(self) -> str:
        return self.area

class Education(models.Model):
    person = models.ForeignKey(User,on_delete = models.CASCADE,null = True,blank = True)
    course = models.CharField(max_length= 100, null = True,blank= True)
    institute = models.CharField(max_length= 150,null = True, blank = True)
    joining  = models.DateField(auto_now_add= False,auto_now = False,null = True, blank = True)
    enddate  = models.DateField(auto_now_add= False,auto_now = False,null = True, blank = True)
    specification = models.CharField(null = True, blank = True, max_length = 200)
    def __str__(self) -> str:
        return self.course


class Certificate(models.Model):
    person = models.ForeignKey(User,on_delete = models.CASCADE,null = True,blank = True)
    title = models.CharField(max_length= 100,null = True,blank= True)
    place = models.CharField(max_length = 150,null = True, blank = True)
    year = models.DateField(null= True,blank = True, auto_now = False, auto_now_add= False)
    def __str__(self) -> str:
        return self.title