from django.db import models
from import_export import resources




class Subject(models.Model):
    name = models.CharField(null=False, max_length=60)

    def __str__(self):
        return self.name
        

class Teacher(models.Model):
    first_name = models.CharField(null=False, max_length=60)
    last_name = models.CharField(null=False, max_length=60)
    profile_picture = models.ImageField(upload_to='', blank=True)
    email_address = models.EmailField(null=False, unique=True, max_length=60)
    phone_number = models.CharField(null=False, max_length=60, blank=True)
    room_number = models.CharField(null=False, max_length=60, blank=True)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.first_name + ' ' + self.last_name



