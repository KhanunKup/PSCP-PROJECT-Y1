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
