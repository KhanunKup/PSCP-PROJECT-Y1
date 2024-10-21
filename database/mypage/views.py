from django.shortcuts import render
from mypage.models import creativereser
from mypage.models import peerone

# Create your views here.
def index(request):
    return render(request,"index.html")

def creative(request):
    return render(request,"creative.html")

def room(request):
    list_person = creativereser.objects.order_by('event_date') #****************
    # list_person = creativereser.objects.all()
    return render(request,"checkscreative.html",{"list_person":list_person})

def room_2(request):
    list_person_2 = peerone.objects.all()
    return render(request,"checkscreative.html",{"list_person_2":list_person_2})