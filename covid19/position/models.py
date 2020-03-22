from django.db import models

# Create your models here.
class pos(models.Model):
    locationName=models.CharField(max_length=30)
    longitude=models.FloatField()
    latitude=models.FloatField()
    infectionTime=models.DateField()
    createdTime=models.DateTimeField(auto_now_add=True)
    changedTime=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.locationName