from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    consultants = models.M


class Consultant(models.Model):
    name = models.CharField(max_length=100)
    brithday = models.DateField()
    organization = models.ForeignKey(Organization, related_name="consultants")
