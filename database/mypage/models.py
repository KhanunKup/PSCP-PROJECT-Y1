from django.db import models

# Create your models here.
class creativereser(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=100)
    event_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_id} {self.name} {self.event_date} {self.end_time}"

class peer1reser(models.Model):
    student_idpeer1 = models.IntegerField()
    namepeer1 = models.CharField(max_length=100)
    event_datepeer1 = models.DateField()
    start_timepeer1 = models.TimeField(null=True, blank=True)
    end_timepeer1 = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_idpeer1} {self.namepeer1} {self.event_datepeer1} {self.end_timepeer1}"
    
class peer2reser(models.Model):
    student_idpeer2 = models.IntegerField()
    namepeer2 = models.CharField(max_length=100)
    event_datepeer2 = models.DateField()
    start_timepeer2 = models.TimeField(null=True, blank=True)
    end_timepeer2 = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_idpeer2} {self.namepeer2} {self.event_datepeer2} {self.end_timepeer2}"