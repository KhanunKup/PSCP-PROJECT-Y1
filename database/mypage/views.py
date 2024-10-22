from django.shortcuts import render,redirect
from django.contrib import messages
from mypage.models import creativereser,peer1reser,peer2reser
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")

def creative(request):
    if request.method == 'POST':
        id_inputpeer1 = request.POST['student-id-form']
        name_inputpeer1 = request.POST['name-form']
        date_input = request.POST['date-form']
        start_input = request.POST['start-date-form']
        end_input = request.POST['end-date-form']

        start_time = datetime.strptime(start_input, '%H:%M').time()
        end_time = datetime.strptime(end_input, '%H:%M').time()

        overlapping_bookings = creativereser.objects.filter(
            event_date=date_input,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).exists()

        if overlapping_bookings:
            messages.error(request, "The room has been booked during that time. Please enter a different time slot!")
            return redirect("creative.html")

        form = creativereser.objects.create(
            student_id=id_inputpeer1,
            name=name_inputpeer1,
            event_date=date_input,
            start_time=start_time,
            end_time=end_time
        )
        form.save()
        return redirect("checkscreative.html")
    else:
        return render(request, "creative.html")

def room(request):
    list_person = creativereser.objects.all()
    list_personpeer1 = peer1reser.objects.all()
    list_personpeer2 = peer2reser.objects.all()
    return render(request,"checkscreative.html",{
        "list_person":list_person,
        "list_personpeer1":list_personpeer1,
        "list_personpeer2":list_personpeer2
        })

def peer1(request):
    if request.method == 'POST':
        id_inputpeer1 = request.POST['student-id-form-peer1']
        name_inputpeer1 = request.POST['name-form-peer1']
        date_inputpeer1 = request.POST['date-form-peer1']
        start_inputpeer1 = request.POST['start-date-form-peer1']
        end_inputpeer1 = request.POST['end-date-form-peer1']

        start_time_1 = datetime.strptime(start_inputpeer1, '%H:%M').time()
        end_time_1 = datetime.strptime(end_inputpeer1, '%H:%M').time()

        overlappingpeer1_bookings = peer1reser.objects.filter(
            event_datepeer1=date_inputpeer1,
            start_timepeer1__lt=end_time_1,
            end_timepeer1__gt=start_time_1
        ).exists()

        if overlappingpeer1_bookings:
            messages.error(request, "The room has been booked during that time. Please enter a different time slot!")
            return redirect("peer1.html")

        form = peer1reser.objects.create(
            student_idpeer1=id_inputpeer1,
            namepeer1=name_inputpeer1,
            event_datepeer1=date_inputpeer1,
            start_timepeer1=start_time_1,
            end_timepeer1=end_time_1
        )
        form.save()
        return redirect("checkscreative.html")
    else:
        return render(request, "peer1.html")

def peer2(request):
    if request.method == 'POST':
        id_inputpeer2 = request.POST['student-id-form-peer2']
        name_inputpeer2 = request.POST['name-form-peer2']
        date_inputpeer2 = request.POST['date-form-peer2']
        start_inputpeer2 = request.POST['start-date-form-peer2']
        end_inputpeer2 = request.POST['end-date-form-peer2']

        start_time_2 = datetime.strptime(start_inputpeer2, '%H:%M').time()
        end_time_2 = datetime.strptime(end_inputpeer2, '%H:%M').time()

        overlappingpeer1_bookings = peer1reser.objects.filter(
            event_datepeer1=date_inputpeer2,
            start_timepeer1__lt=end_time_2,
            end_timepeer1__gt=start_time_2
        ).exists()

        if overlappingpeer1_bookings:
            messages.error(request, "The room has been booked during that time. Please enter a different time slot!")
            return redirect("peer2.html")

        form = peer2reser.objects.create(
            student_idpeer2=id_inputpeer2,
            namepeer2=name_inputpeer2,
            event_datepeer2=date_inputpeer2,
            start_timepeer2=start_time_2,
            end_timepeer2=end_time_2
        )
        form.save()
        return redirect("checkscreative.html")
    else:
        return render(request, "peer2.html")
