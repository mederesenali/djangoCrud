from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def getHomePage(request):
    return HttpResponse("<h1>Tasks</h1>")



def getDoneTasks(request):
    return HttpResponse("<h1>Done Task</h1>")