from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def insert_topic(request):
    TFO=Topicform()
    d={'TFO':TFO}

    if request.method=='POST':
        TD=Topicform(request.POST)
        if TD.is_valid():
            TD.save()
            return HttpResponse('data submited')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WPO=Webpageform()
    d={'WPO':WPO}

    if request.method=='POST':
        WD=Webpageform(request.POST)
        if WD.is_valid():
            WD.save()
            return HttpResponse('data submited')
        

    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    ARO=Accessrecordform()
    d={'ARO':ARO}

    if request.method=='POST':
        AD=Accessrecordform(request.POST)
        if AD.is_valid():
            AD.save()

            return HttpResponse('data submited successfully')

    return render(request,'insert_accessrecord.html',d)
