from django.shortcuts import render,redirect
from django.contrib import messages
from mypage.models import creativereser,peer1reser,peer2reser, peer3reser
from datetime import datetime, timedelta

# Create your views here.
def is_not_integer(value):
    try:
        int(value)
        return False
    except (ValueError, TypeError):
        return True

def index(request):
    return render(request,"index.html")

def room(request):
    list_person = creativereser.objects.order_by('event_date')
    list_personpeer1 = peer1reser.objects.order_by('event_datepeer1')
    list_personpeer2 = peer2reser.objects.order_by('event_datepeer2')
    list_personpeer3 = peer3reser.objects.order_by('event_datepeer3')
    return render(request,"checkscreative.html",{
        "list_person":list_person,
        "list_personpeer1":list_personpeer1,
        "list_personpeer2":list_personpeer2,
        "list_personpeer3": list_personpeer3
        })

def creative(request):
    if request.method == 'POST':
        id_input = request.POST['student-id-form']
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

        diff_time = datetime.strptime(start_input, '%H:%M') - datetime.strptime(end_input, '%H:%M')
        exceed_3hr_bookings = abs(diff_time) > timedelta(hours=3)

        if is_not_integer(id_input):
            messages.error(request, "Invalid input: Student ID must be an integer!")
            return redirect("creative.html")

        if exceed_3hr_bookings:
            messages.error(request, "The room has been more than 3 hours. Please enter a different time slot!")
            return redirect("creative.html")

        if overlapping_bookings:
            messages.error(request, "The room has been booked during that time. Please enter a different time slot!")
            return redirect("creative.html")
        form = creativereser.objects.create(
            student_id=id_input,
            name=name_inputpeer1,
            event_date=date_input,
            start_time=start_time,
            end_time=end_time
        )
        form.save()
        return redirect("checkscreative.html")
    else:
        return render(request, "creative.html")


def peer1(request):
    if request.method == 'POST':
        id_inputpeer1 = request.POST['student-id-form-peer1']
        name_inputpeer1 = request.POST['name-form-peer1']
        date_inputpeer1 = request.POST['date-form-peer1']
        start_inputpeer1 = request.POST['start-date-form-peer1']
        end_inputpeer1 = request.POST['end-date-form-peer1']

        start_time_1 = datetime.strptime(start_inputpeer1, '%H:%M').time()
        end_time_1 = datetime.strptime(end_inputpeer1, '%H:%M').time()

        overlapping_bookings = peer1reser.objects.filter(
            event_datepeer1=date_inputpeer1,
            start_timepeer1__lt=end_time_1,
            end_timepeer1__gt=start_time_1
        ).exists()

        diff_time = datetime.strptime(start_inputpeer1, '%H:%M') - datetime.strptime(start_inputpeer1, '%H:%M')
        exceed_3hr_bookings = abs(diff_time) > timedelta(hours=3)

        if is_not_integer(id_inputpeer1):
            messages.error(request, "Invalid input: Student ID must be an integer!")
            return redirect("creative.html")

        if exceed_3hr_bookings:
            messages.error(request, "The room has been more than 3 hours. Please enter a different time slot!")
            return redirect("creative.html")

        if overlapping_bookings:
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

        overlapping_bookings = peer2reser.objects.filter(
            event_datepeer2=date_inputpeer2,
            start_timepeer2__lt=end_time_2,
            end_timepeer2__gt=start_time_2
        ).exists()

        diff_time = datetime.strptime(start_inputpeer2, '%H:%M') - datetime.strptime(end_inputpeer2, '%H:%M')
        exceed_3hr_bookings = abs(diff_time) > timedelta(hours=3)

        if is_not_integer(id_inputpeer2):
            messages.error(request, "Invalid input: Student ID must be an integer!")
            return redirect("peer2.html")

        if exceed_3hr_bookings:
            messages.error(request, "The room has been more than 3 hours. Please enter a different time slot!")
            return redirect("peer2.html")

        if overlapping_bookings:
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

def peer3(request):
    if request.method == 'POST':
        id_inputpeer3 = request.POST['student-id-form-peer3']
        name_inputpeer3 = request.POST['name-form-peer3']
        date_inputpeer3 = request.POST['date-form-peer3']
        start_inputpeer3 = request.POST['start-date-form-peer3']
        end_inputpeer3 = request.POST['end-date-form-peer3']

        start_time_3 = datetime.strptime(start_inputpeer3, '%H:%M').time()
        end_time_3 = datetime.strptime(end_inputpeer3, '%H:%M').time()

        overlapping_bookings = peer3reser.objects.filter(
            event_datepeer3=date_inputpeer3,
            start_timepeer3__lt=end_time_3,
            end_timepeer3__gt=start_time_3
        ).exists()

        diff_time = datetime.strptime(start_inputpeer3, '%H:%M') - datetime.strptime(end_inputpeer3, '%H:%M')
        exceed_3hr_bookings = abs(diff_time) > timedelta(hours=3)

        if is_not_integer(id_inputpeer3):
            messages.error(request, "Invalid input: Student ID must be an integer!")
            return redirect("peer3.html")

        if exceed_3hr_bookings:
            messages.error(request, "The room has been more than 3 hours. Please enter a different time slot!")
            return redirect("peer3.html")

        if overlapping_bookings:
            messages.error(request, "The room has been booked during that time. Please enter a different time slot!")
            return redirect("peer3.html")

        form = peer3reser.objects.create(
            student_idpeer3=id_inputpeer3,
            namepeer3=name_inputpeer3,
            event_datepeer3=date_inputpeer3,
            start_timepeer3=start_time_3,
            end_timepeer3=end_time_3
        )
        form.save()
        return redirect("checkscreative.html")
    else:
        return render(request, "peer3.html")

