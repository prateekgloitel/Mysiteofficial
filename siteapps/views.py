
from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    educationdetails = Education.objects.all()
    workdetails = WorkExperience.objects.all()
    persondetails = User.objects.all()
    projectdetails = Project.objects.all()
    intrests = Intrest.objects.all()
    work = workdetails.count()
    project = projectdetails.count()
    profiledata = {
        'educationdetails': educationdetails,
        'workdetails':workdetails,
        'person':persondetails,
        'projects':projectdetails,
        'workcount':work,
        'projectcount':project,
        'intrests':intrests,
    }
    return render(request, 'index.html', profiledata)

