from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.PositiveIntegerField()
    class Meta:
        db_table="Register"
class contactus(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    email = models.EmailField(primary_key=True)
    comment = models.CharField(max_length=225)
    class Meta:
        db_table="contactus"


