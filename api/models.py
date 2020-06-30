from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Organization:{self.name}>"


class Consultant(models.Model):
    name = models.CharField(max_length=100)
    brithday = models.DateField()
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="consultants"
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Consultant:{self.name}>"
