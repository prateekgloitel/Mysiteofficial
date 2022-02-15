
from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    educationdetails = Education.objects.all()
    workdetails = WorkExperience.objects.all()
    persondetails = User.objects.all()
    projectdetails = Project.objects.all()
    profiledata = {
        'educationdetails': educationdetails,
        'workdetails':workdetails,
        'person':persondetails,
        'projects':projectdetails,
    }
    return render(request, 'index.html', profiledata)

 # 
    # skills = Skill.objects.all()
    # intrests = Intrest.objects.all()
    # certificates = Certificate.objects.all()
    # projectdetails = Project.objects.all()
    # 
#   'projectdetails':projectdetails,
#         
    #  'person':persondetails,
    # 'skills':skills,
    # 'intrests':intrests,
    # 'certificates':certificates,


# def certification(request):
#     certificates = Certificate.objects.all()
#     certificatedata ={
#         'certificates':certificates
#     }
#     return render(request,"index.html",certificatedata)


# def educations(request):
#     details = Education.objects.all()
#     educationdata = {
#         'educations':details
#     }
#     return render(request,"index.html",educationdata)


# def projects(request):
#     details = Project.objects.all()
#     projectdata = {
#         "projects":details
#     }
#     return render(request,"index.html",projectdata)


# def workExperience(request):
#     details = WorkExperience.objects.all()
#     workdata={
#         "workexp":details,
#     }
#     return render(request,"index.html",workdata)
