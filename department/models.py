from django.db import models

# Create your models here.
from django.db import models

class HospitalDepartment(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='departments/', null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    picture = models.ImageField(upload_to='doctors/', blank=True, null=True)
    department = models.ForeignKey(HospitalDepartment, null=True, on_delete=models.SET_NULL)
    designation = models.CharField(max_length=255, blank=True, null=True)
    registration_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    

class OPD_Schedule(models.Model):
    department = models.ForeignKey(HospitalDepartment, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    room_no = models.CharField(max_length=255)
    visiting_days = models.CharField(max_length=500)  
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "OPD Schedule"
        verbose_name_plural = "OPD Schedules"

    def __str__(self):
        return f"{self.doctor.name} - {self.department.name} (Room: {self.room_no})"
    
