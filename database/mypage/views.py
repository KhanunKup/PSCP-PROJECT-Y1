from django.shortcuts import render,redirect
from mypage.models import creativereser
from mypage.models import peerone

# Create your views here.
def index(request):
    return render(request,"index.html")

def creative(request):
    if request.method == 'POST':
        id_input = request.POST['student-id-form']
        name_input = request.POST['name-form']
        date_input = request.POST['date-form']

        form = creativereser.objects.create(
            student_id = id_input,
            name = name_input,
            event_date = date_input
        )
        form.save()
        return redirect("checkscreative.html")
    else:
        return render(request,"creative.html")

def room(request):
    list_person = creativereser.objects.all()
    return render(request,"checkscreative.html",{"list_person":list_person})

def room_2(request):
    list_person_2 = peerone.objects.all()
    return render(request,"checkscreative.html",{"list_person_2":list_person_2})
