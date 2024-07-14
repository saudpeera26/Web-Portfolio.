from django.shortcuts import render
from .models import MyFrontEndSKills, MyBackEndSKills
from .models import MyProjects

# Create your views here.


def homePage(request):
    frontEndSkills = MyFrontEndSKills.objects.all()
    backEndSkills = MyBackEndSKills.objects.all()
    projects = MyProjects.objects.all()
    context = {
        "frontEndSkills" : frontEndSkills,
        "backEndSkills" : backEndSkills,
        "projects" : projects

    }
    return render(request, "home.html", context)
