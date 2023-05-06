from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Venue(models.Model):
        name = models.CharField(max_length=120)
        address = models.CharField(max_length=300)
        zip_code = models.CharField(max_length=15)
        phone = models.CharField(max_length=25,blank=True)
        web = models.URLField(blank=True)
        email_address = models.EmailField(blank=True)

        def __str__(self) -> str:
             return self.name

class MyClubUser(models.Model):
     first_name = models.CharField(max_length=120)
     last_name = models.CharField(max_length=120)
     email = models.EmailField()

     def __str__(self) -> str:
          return self.first_name + " " + self.last_name
class Events(models.Model):
    name = models.CharField('Event Name',max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue,on_delete=models.CASCADE,blank=True,null=True)
    manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser,blank=True)

    def __str__(self) -> str:
        return self.name