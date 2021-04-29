from .models import elecbill
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Elecbill.forms import Elecform

# Create your views here.

def index(request):
    dests = elecbill.objects.all()
    return render(request,'edit.html',{'dests':dests})


def showbill(request):
    showall=elecbill.objects.all()
    return render(request, 'index.html',{"data":showall})


def insertbill(request):
    if request.method == "POST":
        if request.POST.get('c_name') and request.POST.get('c_id') and request.POST.get('c_img') and request.POST.get('c_email') and request.POST.get('c_date') and request.POST.get('c_city') and request.POST.get('c_address') and request.POST.get('utility') and request.POST.get('units') and request.POST.get('bill') and request.POST.get('copy'):
            saverecord=elecbill()
            saverecord.c_name=request.POST.get('c_name')
            saverecord.c_id=request.POST.get('c_id')
            saverecord.c_img=request.POST.get('c_img')
            saverecord.c_email=request.POST.get('c_email')
            saverecord.c_date=request.POST.get('c_date')
            saverecord.c_city=request.POST.get('c_city')
            saverecord.c_address=request.POST.get('c_address')
            saverecord.utility=request.POST.get('utility')
            saverecord.units=request.POST.get('units')
            saverecord.bill=request.POST.get('bill')
            saverecord.copy=request.POST.get('copy')
            saverecord.save()
            messages.success(request,'Bill Generated.')
            return render(request,'insert.html')
    else:
            return render(request,'insert.html')

def updatebill(request,id):
    Updatebill=elecbill.objects.get(id=id)
    return render(request, 'edit.html',{"elecbill":Updatebill})

def editbutton(request,id):

    Editbutton=elecbill.objects.get(id=id)
    form=Elecform(request.POST,instance=Editbutton)
    if form.is_valid():
        form.save()
        messages.success(request,'Bill Updated')
        return render(request,'edit.html',{"elecbill": Editbutton})

def delbill(request,id):
    delelecbill=elecbill.objects.get(id=id)
    delelecbill.delete()
    showdata=elecbill.objects.all()
    return render(request,'index.html',{"data": showdata})