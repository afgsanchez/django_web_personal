from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request): # pylint: disable=missing-function-docstring
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects':projects})

