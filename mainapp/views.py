from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView

from django.contrib.auth.forms import User
# from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, "home.html")

def projects(request):
    return render(request, "projects.html")


